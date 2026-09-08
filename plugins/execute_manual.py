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

import re
import sys
import datetime
from collections.abc import Iterator
from typing import Optional

import tmt
import tmt.log
import tmt.steps
import tmt.steps.execute
from tmt.container import container, field
from tmt.guest import Guest
from tmt.result import Result, ResultOutcome
from tmt.steps.execute import TestInvocation
from tmt.steps.discover import DiscoverPlugin
from tmt.utils import Environment, Path


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


def prompt_result(step_num: int, total: int) -> str:
    """Prompt the tester for a step result."""
    valid = {'p': 'pass', 'f': 'fail', 's': 'skip', 'a': 'abort'}
    while True:
        try:
            answer = input(
                f"  Step {step_num}/{total} result "
                f"[\033[32mp\033[0m]ass / "
                f"[\033[31mf\033[0m]ail / "
                f"[\033[33ms\033[0m]kip / "
                f"[\033[91ma\033[0m]bort: "
            ).strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return 'abort'
        if answer in valid:
            return valid[answer]
        if answer in valid.values():
            return answer
        print(f"  Please enter one of: p, f, s, a")


SEPARATOR = "\033[90m" + "─" * 72 + "\033[0m"
BOLD = "\033[1m"
RESET = "\033[0m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
DIM = "\033[2m"


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
    ) -> Iterator[tuple[Optional[str], list['Guest']]]:
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
        guest: 'Guest',
        environment: Optional[Environment] = None,
        logger: tmt.log.Logger,
    ) -> None:
        super().go(guest=guest, environment=environment, logger=logger)

        if self.is_dry_run:
            self._results = []
            return

        test_invocations = self.prepare_tests(guest, logger)

        for index, invocation in enumerate(test_invocations):
            test = invocation.test
            invocation.start_time = tmt.utils.format_timestamp(
                datetime.datetime.now(datetime.timezone.utc))

            test_progress = f"[{index + 1}/{len(test_invocations)}]"

            if not test.node.get('manual', False):
                print(f"\n{SEPARATOR}")
                print(f"  {DIM}{test_progress} Skipping non-manual test: {test.name}{RESET}")
                invocation.end_time = tmt.utils.format_timestamp(
                    datetime.datetime.now(datetime.timezone.utc))
                invocation.real_duration = "00:00:00"
                self._results.append(Result.from_test_invocation(
                    invocation=invocation,
                    result=ResultOutcome.SKIP,
                    note=["non-manual test skipped by manual executor"],
                ))
                self.step.plan.execute.update_results(self.results())
                continue

            test_path = invocation.test.path
            md_file = test.node.get('test', 'manual.md')
            md_path = Path(self.step.plan.worktree) / test_path.unrooted() / md_file

            if not md_path.exists():
                md_path = Path(self.step.plan.discover.workdir) / test_path.unrooted() / md_file

            if not md_path.exists():
                invocation.end_time = tmt.utils.format_timestamp(
                    datetime.datetime.now(datetime.timezone.utc))
                invocation.real_duration = "00:00:00"
                self._results.append(Result.from_test_invocation(
                    invocation=invocation,
                    result=ResultOutcome.ERROR,
                    note=[f"manual test file not found: {md_file}"],
                ))
                self.step.plan.execute.update_results(self.results())
                continue

            steps = parse_manual_md(md_path)

            print(f"\n{SEPARATOR}")
            print(f"  {BOLD}{test_progress} {test.summary or test.name}{RESET}")
            if test.node.get('description'):
                print(f"  {DIM}{test.node.get('description')}{RESET}")
            print(f"  {DIM}ID: {test.node.get('id', 'N/A')} | "
                  f"Tags: {', '.join(test.node.get('tag', []))}{RESET}")
            print(f"  {DIM}{len(steps)} step(s) to execute{RESET}")
            print(SEPARATOR)

            step_results = []
            aborted = False

            for step_num, step_data in enumerate(steps, 1):
                step_text = step_data.get('step', '')
                expect_text = step_data.get('expect', '')

                print(f"\n  {CYAN}{BOLD}Step {step_num}/{len(steps)}{RESET}")
                for line in step_text.split('\n'):
                    print(f"  {line}")

                if expect_text:
                    print(f"\n  {GREEN}{BOLD}Expected:{RESET}")
                    for line in expect_text.split('\n'):
                        print(f"  {line}")

                print()
                result = prompt_result(step_num, len(steps))

                if result == 'abort':
                    step_results.append('fail')
                    aborted = True
                    print(f"  {YELLOW}Test aborted by tester.{RESET}")
                    break
                step_results.append(result)

            invocation.end_time = tmt.utils.format_timestamp(
                datetime.datetime.now(datetime.timezone.utc))
            start = datetime.datetime.fromisoformat(invocation.start_time)
            end = datetime.datetime.fromisoformat(invocation.end_time)
            duration = end - start
            hours, remainder = divmod(int(duration.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            invocation.real_duration = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

            if any(r == 'fail' for r in step_results):
                outcome = ResultOutcome.FAIL
                failed_steps = [i + 1 for i, r in enumerate(step_results) if r == 'fail']
                note = [f"failed step(s): {', '.join(str(s) for s in failed_steps)}"]
            elif all(r == 'skip' for r in step_results):
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

            print(f"\n  Result: {outcome_color}{BOLD}{outcome.value}{RESET}"
                  f" ({invocation.real_duration})")
            print(SEPARATOR)

            self._results.append(Result.from_test_invocation(
                invocation=invocation,
                result=outcome,
                note=note or None,
            ))
            self.step.plan.execute.update_results(self.results())

    def results(self) -> list[Result]:
        return self._results
