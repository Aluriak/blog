"""
separator
===================================

This Pelican-Markdown plugin place space before titles.
(except the first)

"""


import re
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension


class SeparatorExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        # Insert SeparatorPreprocessor instance into markdown preprocessors
        md.preprocessors.add('separator', SeparatorPreprocessor(), '_begin')


class SeparatorPreprocessor(Preprocessor):
    """Add a constant separator before titles"""

    SEPARATOR = {  # level: separator
        1: '<br>\n<hr>\n',
        2: '<br>\n',
    }
    REG_TITLE = re.compile(r'^([#]+)')

    def run(self, lines):
        self.first = True
        return [self.converted(line) for line in lines]

    def converted(self, line) -> 'line':
        match = SeparatorPreprocessor.REG_TITLE.match(line)
        if match:
            if self.first:
                self.first = False
                return line
            level = len(match.groups(0)[0])
            return SeparatorPreprocessor.SEPARATOR.get(level, '') + line
        return line
