"""
checkbox
===================================

This Pelican-Markdown plugin replace github like markdown notation of checkbox by html code.
"""

import re
import markdown as md
from markdown.inlinepatterns import Pattern
from markdown.extensions import Extension
import xml.etree.ElementTree as etree


BOX_PATTERN = r'\[([ a-z-]+)\]'
# icônes font awesome 6 ; [nom] sans raccourci donne fa-solid fa-<nom>
ICONS_SHORTCUT = {
    ' ': 'fa-regular fa-square',
    'v': 'fa-regular fa-square-check',
    'x': 'fa-solid fa-xmark',
    'n': 'fa-solid fa-xmark',
    'l': 'fa-solid fa-link',
    's': 'fa-solid fa-shuttle-space',
    'g': 'fa-brands fa-gitlab',
    't': 'fa-solid fa-terminal',
    '+': 'fa-solid fa-plus',
    '-': 'fa-solid fa-minus',
    'o': 'fa-solid fa-circle-check',
    'b': 'fa-solid fa-bomb',
    '»': 'fa-solid fa-caret-right',
    '«': 'fa-solid fa-caret-left',
    '>': 'fa-solid fa-chevron-right',
    '<': 'fa-solid fa-chevron-left',
}


class BoxPattern(Pattern):
    def handleMatch(self, m):
        boxcontent = m.group(2)
        box_name = ICONS_SHORTCUT.get(boxcontent, 'fa-solid fa-' + boxcontent)
        el = etree.Element('i', {'class': '{} fa-fw'.format(box_name)})
        el.text = ''
        return el


class BoxExtension(Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(BoxPattern(BOX_PATTERN), 'boxpattern', 1)
