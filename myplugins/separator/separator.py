"""
separator
===================================

This Pelican-Markdown plugin place space before titles.
(except the first)

"""

import re
import markdown as md
from markdown.inlinepatterns import Pattern
from markdown.extensions import Extension
from markdown.util import etree


DEFAULT_SEPARATOR = '<br>\n'
SEPARATOR = {  # level: separator
    1: '<br>\n<br>\n<hr>\n',
    2: '<br>\n',
}
TITLE_PATTERN = re.compile(r'^([#]+)')


class TitleSepPattern(Pattern):
    """Add a constant separator before titles"""
    def handleMatch(self, m):
        print('STPLDE:', m.groups())
        level = len(m.group(2))
        el = etree.Element('')
        el.text = SEPARATOR.get(level, DEFAULT_SEPARATOR) + line
        return el


class TitleSepExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('titleseppattern', TitleSepPattern(TITLE_PATTERN), '_end')
