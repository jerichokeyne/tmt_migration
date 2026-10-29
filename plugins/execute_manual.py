"""
tmt execute plugin for interactive manual test execution.

Presents manual test steps to a human tester in the terminal and
prompts for pass/fail/skip per step. Automated tests (manual: false)
are skipped with a note.

Usage in a plan:

    execute:
        how: manual

Load via: TMT_PLUGINS=/path/to/plugins tmt run ...
"""

import datetime
import re
from collections.abc import Iterator

import tmt
import tmt.log
import tmt.steps
import tmt.steps.execute
from rich.console import Console, Group
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from tmt.container import container
from tmt.guest import Guest
from tmt.result import Result, ResultOutcome
from tmt.steps.discover import DiscoverPlugin
from tmt.utils import Environment, Path

console = Console(highlight=False)


def parse_manual_md(path: Path) -> list[dict[str, str]]:
    """
    Parse a tmt manual test Markdown file into a list of step/expect pairs.

    Returns a list of dicts like:
        [{"step": "Do this", "expect": "See that"}, ...]
    """
    content = path.read_text()
    lines = content.split('\n')

    steps = []
    current_section = None
    current_text = []
    current_step = {}

    for line in lines:
        stripped = line.strip()

        heading_match = re.match(r'^##\s+(.*)', stripped)
        if heading_match:
            heading = heading_match.group(1).strip().lower()

            if current_section and current_text:
                text = '\n'.join(current_text).strip()
                if current_section == 'step':
                    if current_step.get('step'):
                        steps.append(current_step)
                        current_step = {}
                    current_step['step'] = text
                elif current_section in ('expect', 'result', 'expected result'):
                    current_step['expect'] = text

            current_text = []
            if heading in ('step', 'test step'):
                current_section = 'step'
            elif heading in ('expect', 'result', 'expected result'):
                current_section = 'expect'
            else:
                current_section = None
            continue

        h1_match = re.match(r'^#\s+(.*)', stripped)
        if h1_match:
            if current_section and current_text:
                text = '\n'.join(current_text).strip()
                if current_section == 'step':
                    current_step['step'] = text
                elif current_section in ('expect', 'result', 'expected result'):
                    current_step['expect'] = text
            if current_step.get('step'):
                steps.append(current_step)
                current_step = {}
            current_section = None
            current_text = []
            continue

        if current_section:
            current_text.append(line)

    if current_section and current_text:
        text = '\n'.join(current_text).strip()
        if current_section == 'step':
            current_step['step'] = text
        elif current_section in ('expect', 'result', 'expected result'):
            current_step['expect'] = text

    if current_step.get('step'):
        steps.append(current_step)

    return steps


@container
class ExecuteManualData(tmt.steps.execute.ExecuteStepData):
    pass


@tmt.steps.provides_method('manual')
class ExecuteManual(tmt.steps.execute.ExecutePlugin[ExecuteManualData]):
    """
    Interactive manual test executor.

    Presents each manual test's steps to the tester in the terminal
    and prompts for pass/fail/skip per step. The overall test result
    is determined by the worst step outcome (any fail = test fails,
    all skip = test skipped, otherwise pass).

    Automated tests (``manual: false``) are skipped with a note.

    .. code-block:: yaml

        execute:
            how: manual
    """

    _data_class = ExecuteManualData

    @property
    def tasks(
        self,
    ) -> Iterator[tuple[str | None, list[Guest]]]:
        for discover in self.step.plan.discover.phases(classes=(DiscoverPlugin,)):
            if not discover.enabled_by_when:
                continue
            yield (
                discover.name,
                [
                    guest
                    for guest in self.step.plan.provision.ready_guests
                    if discover.enabled_on_guest(guest)
                ],
            )

    def go(
        self,
        *,
        guest: Guest,
        environment: Environment | None = None,
        logger: tmt.log.Logger,
    ) -> None:
        super().go(guest=guest, environment=environment, logger=logger)

        if self.is_dry_run:
            self._results = []
            return

        test_invocations = self.prepare_tests(guest, logger)

        for index, invocation in enumerate(test_invocations):
            test = invocation.test
            invocation.stopwatch.start_time = datetime.datetime.now(datetime.UTC)

            test_progress = f"[{index + 1}/{len(test_invocations)}]"

            if not test.node.get('manual', False):
                console.rule()
                console.print(f"  {test_progress} Skipping non-manual test: {test.name}", style="dim")
                console.rule()
                invocation.stopwatch.end_time = datetime.datetime.now(datetime.UTC)
                self._results.append(Result.from_test_invocation(
                    invocation=invocation,
                    result=ResultOutcome.SKIP,
                    note=["non-manual test skipped by manual executor"],
                ))
                self.step.plan.execute.update_results(self.results())
                continue

            test_path = invocation.test.path
            md_file: str = test.node.get('test', 'manual.md')
            md_path:Path = self.step.plan.worktree / test_path.unrooted() / md_file

            if not md_path.exists():
                md_path: Path = self.step.plan.discover.workdir / test_path.unrooted() / md_file

            if not md_path.exists():
                invocation.stopwatch.end_time = datetime.datetime.now(datetime.UTC)
                self._results.append(Result.from_test_invocation(
                    invocation=invocation,
                    result=ResultOutcome.ERROR,
                    note=[f"manual test file not found: {md_file}"],
                ))
                self.step.plan.execute.update_results(self.results())
                continue

            steps = parse_manual_md(md_path)

            header = Group(
                Text(f"{test_progress} {test.summary or test.name}", style="dim"),
                Text(test.node.get("description", ""), style="dim"),
                Text("ID: " + test.node.get("id", "N/A"), style="dim"),
                Text("Tags: " + ', '.join(test.node.get('tag', [])), style="dim"),
                Text(f"{len(steps)} step(s) to execute", style="dim"),
            )
            console.print(header)

            step_results = []
            aborted = False

            for step_num, step_data in enumerate(steps, 1):
                step_text = step_data.get('step', '')
                expect_text = step_data.get('expect', '')

                console.print(Panel(Markdown(step_text), title=f"[bold cyan]Step {step_num}/{len(steps)}[/bold cyan]"))

                if expect_text:
                    console.print(Panel(Markdown(expect_text), title="[bold green]Expected[/bold green]"))

                console.print()
                result = Prompt.ask(f"  Step {step_num}/{len(steps)} result [green]p[/green]ass [red]f[/red]ail [yellow]s[/yellow]kip [bold red]a[/bold red]bort", choices=["p", "f", "s", "a"], case_sensitive=False)

                if result == 'a':
                    step_results.append('fail')
                    aborted = True
                    console.print("  Test aborted by tester.", style="yellow")
                    break
                step_results.append(result)

            invocation.stopwatch.end_time = datetime.datetime.now(datetime.UTC)

            if any(r == 'f' for r in step_results):
                outcome = ResultOutcome.FAIL
                failed_steps = [i + 1 for i, r in enumerate(step_results) if r == 'fail']
                note = [f"failed step(s): {', '.join(str(s) for s in failed_steps)}"]
            elif all(r == 's' for r in step_results):
                outcome = ResultOutcome.SKIP
                note = ["all steps skipped"]
            else:
                outcome = ResultOutcome.PASS
                note = []

            if aborted:
                note.append("aborted by tester")

            outcome_color = {
                ResultOutcome.PASS: "\033[32m",
                ResultOutcome.FAIL: "\033[31m",
                ResultOutcome.SKIP: "\033[33m",
            }.get(outcome, "")

            console.print(Panel(f"\n  Result: {outcome_color}[bold]{outcome.value}[/bold]"
                  f" ({invocation.stopwatch.duration_formatted})"))

            self._results.append(Result.from_test_invocation(
                invocation=invocation,
                result=outcome,
                note=note or None,
            ))
            self.step.plan.execute.update_results(self.results())

    def results(self) -> list[Result]:
        return self._results
