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


DEFAULT_SEPARATOR = '\n<br>'
SEPARATOR = {  # level: separator
    1: '\n<br>ABRIBUS<br><br><hr>',
    2: '\n<br>ABRIBUS<br><br>',
    2: '\n<br>',
}
TITLE_PATTERN = re.compile(r'^([#]+)')
assert TITLE_PATTERN.match('# test')
assert TITLE_PATTERN.match('## test')


class TitleSepPattern(Pattern):
    """Add a constant separator before titles"""
    def handleMatch(self, m):
        print('#' * 100)
        print('STPLDE:', m.groups())
        exit(1)
        level = len(m.group(2))
        el = etree.Element('')
        el.text = SEPARATOR.get(level, DEFAULT_SEPARATOR)
        return el


class TitlesepExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('titleseppattern', TitleSepPattern(TITLE_PATTERN), '_end')
