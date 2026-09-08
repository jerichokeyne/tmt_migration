"""
tmt discover plugin that includes manual tests in discovery.

The built-in 'fmf' discover plugin hardcodes `conditions=["manual is False"]`,
which excludes all tests with `manual: true` from plans. This plugin removes
that restriction so manual tests can be discovered alongside automated ones.

Usage in a plan:

    discover:
        how: fmf-manual

Load via: TMT_PLUGINS=/path/to/plugins tmt run ...
"""

import re
from typing import Optional

import fmf

import tmt
import tmt.base.core
import tmt.base.links
import tmt.steps
import tmt.steps.discover
import tmt.steps.discover.fmf as discover_fmf
from tmt.utils import Path


@tmt.steps.provides_method('fmf-manual')
class DiscoverFmfManual(discover_fmf.DiscoverFmf):
    """
    Discover tests from fmf metadata, including manual tests.

    Identical to ``discover --how fmf`` except that tests with
    ``manual: true`` are no longer excluded from discovery.

    .. code-block:: yaml

        discover:
            how: fmf-manual
            filter: 'tag:ocm-role & tag:ManualOnly'
    """

    def do_the_discovery(self, path: Optional[Path] = None) -> list['tmt.base.core.Test']:
        path = path or Path('')
        tree_path = self.test_dir / path.unrooted()
        if not tree_path.is_dir():
            raise tmt.utils.DiscoverError(f"Metadata tree path '{path}' not found.")

        filters = list(tmt.base.core.Test._opt('filters') or self.get('filter', []))
        for filter_ in filters:
            self.info('filter', filter_, 'green')
        if self.data.test:
            self.info('tests', fmf.utils.listed([test.name for test in self.data.test]), 'green')

        raw_link_needles = list(tmt.Test._opt('links', []) or self.get('link', []))
        link_needles = [
            tmt.base.links.LinkNeedle.from_spec(raw_needle) for raw_needle in raw_link_needles
        ]
        for link_needle in link_needles:
            self.info('link', str(link_needle), 'green')

        excludes = list(tmt.base.core.Test._opt('exclude') or self.data.exclude)
        includes = list(tmt.base.core.Test._opt('include') or self.data.include)

        modified_only = self.get('modified-only')
        modified_url = self.get('modified-url')
        if modified_url:
            previous = modified_url
            modified_url = tmt.utils.git.clonable_git_url(modified_url)
            self.info('modified-url', modified_url, 'green')
            if previous != modified_url:
                self.debug(f"Original url was '{previous}'.")
            self.debug(f"Fetch also '{modified_url}' as 'reference'.")
            self.run(
                tmt.utils.Command('git', 'remote', 'add', 'reference', modified_url),
                cwd=self.test_dir,
            )
            self.run(
                tmt.utils.Command('git', 'fetch', 'reference'),
                cwd=self.test_dir,
            )
        if modified_only:
            modified_ref = self.get(
                'modified-ref',
                tmt.utils.git.default_branch(repository=self.test_dir, logger=self._logger),
            )
            self.info('modified-ref', modified_ref, 'green')
            ref_commit = self.run(
                tmt.utils.Command('git', 'rev-parse', '--short', str(modified_ref)),
                cwd=self.test_dir,
            )
            assert ref_commit.stdout is not None
            self.verbose('modified-ref hash', ref_commit.stdout.strip(), 'green')
            output = self.run(
                tmt.utils.Command(
                    'git', 'log', '--format=', '--stat', '--name-only', f"{modified_ref}..HEAD"
                ),
                cwd=self.test_dir,
            )
            if output.stdout:
                directories = [Path(name).parent for name in output.stdout.split('\n')]
                modified = {
                    f"^/{re.escape(str(directory))}($|/)"
                    for directory in directories
                    if directory
                }
                if not modified:
                    return []
                self.debug(f"Limit to modified test dirs: {modified}", level=3)
                self.data.test.extend(
                    discover_fmf.TestsWithAdjusts(name=name) for name in modified
                )
            else:
                self.debug(f"No modified directories between '{modified_ref}..HEAD' found.")
                return []

        self.debug(f"Check metadata tree in '{tree_path}'.")
        tests = []
        tree = tmt.Tree(
            logger=self._logger,
            path=tree_path,
            fmf_context=self.step.plan.fmf_context,
            additional_rules=self.data.adjust_tests,
        )
        if not self.data.test or not any(test.adjust_rule for test in self.data.test):
            tests += tree.tests(
                filters=filters,
                names=[test.name for test in self.data.test],
                conditions=[],
                unique=False,
                links=link_needles,
                includes=includes,
                excludes=excludes,
            )
        else:
            for test in self.data.test:
                if test.adjust_rule:
                    adjusted_tree = tmt.Tree(
                        logger=self._logger,
                        path=tree_path,
                        fmf_context=self.step.plan.fmf_context,
                        additional_rules=[*self.data.adjust_tests, test.adjust_rule],
                    )
                else:
                    adjusted_tree = tree
                tests += adjusted_tree.tests(
                    filters=filters,
                    names=[test.name],
                    conditions=[],
                    unique=False,
                    links=link_needles,
                    includes=includes,
                    excludes=excludes,
                )
        return tests
