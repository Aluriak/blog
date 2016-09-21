"""
checkbox
===================================

This Pelican-Markdown plugin replace github like markdown notation of checkbox by html code.
"""


import re
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension


class CheckBoxExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        # Insert CheckBoxPreprocessor instance into markdown preprocessors
        md.preprocessors.add('del', CheckBoxPreprocessor(), '_begin')


class CheckBoxPreprocessor(Preprocessor):
    """Replace occurrences of [ ] and [x] by html code"""

    CHECK_BOX_REGEX = re.compile(r'\[([ xX])\]')
    CHECKED = '<i class="icon-check-square-o"></i>'
    UNCHECKED = '<i class="icon-square-o"></i>'
    LARGE_CHECKED = '<i class="icon-check-square-o icon-large"></i>'
    LARGE_UNCHECKED = '<i class="icon-square-o icon-large"></i>'

    def run(self, lines):
        return [self.converted(line) for line in lines]

    def converted(self, line):
        return self.CHECK_BOX_REGEX.sub(
            CheckBoxPreprocessor.checkbox_object,
            line
        )

    @staticmethod
    def checkbox_object(matchobj):
        if matchobj.groups()[0] == ' ':
            return CheckBoxPreprocessor.UNCHECKED
            # return '{{ CHECKBOX_UNCHECK_HTML }}'
        return CheckBoxPreprocessor.CHECKED
        # return '{{ CHECKBOX_CHECKED_HTML }}'
