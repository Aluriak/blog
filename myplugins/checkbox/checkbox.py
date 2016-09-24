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


def regex_id_from_icon_names(names):
    kept = ''
    for name in names:
        kept += name
        if name.upper() != name:
            kept += name.upper()
    return re.escape(kept + '12345!?')


class CheckBoxPreprocessor(Preprocessor):
    """Replace occurrences of [ ] and [x] by html code

    Use FontAwesome in order to replace the github feature of checkbox,
    but allows multiple icons (using stack feature of font awesome):

        [2 1t]  -> 2xsized empty square (`2 `) under terminal 1xsized (`1t`)

    Initial size is 1 (normal), and can be modified using numbers 2, 3, 4 or 5.
    letters and some special characters lead to particular font awesome icons.
    See ICONS mapping for exact definition.
    If the last char is a size, it gives the size of the stack.

    As in github, [ ] stands for empty checkbox, and [x] for the checked one.
    [X] is also a checked one, but using the fa-large flag (size +33%).

    Other chars:
        '!' set the size to +33% (works only as last char if multiple icons)
        '?' (un)set the char reversion (black&white -> white&black)


    See http://fontawesome.io/examples/ for more details on font awesome.

    """

    ICONS = {
        ' ': 'square-o',
        'x': 'check-square-o',
        'l': 'link',
        's': 'space-shuttle',
        'g': 'gitlab',
        't': 'terminal',
        '+': 'plus',
        '-': 'minus',
        'o': 'ok-sign',
        'b': 'bomb',
    }
    CHECK_BOX_REGEX = re.compile(
        r'\[([{}]+)\]'.format(regex_id_from_icon_names(ICONS))
    )
    TEMPLATE_SPAN = '<span class="fa-stack {}">{}</span>'  # size, icons
    TEMPLATE_ICON = '<i class="fa{}{}{}"></i>'


    def run(self, lines:iter) -> iter:
        """Method called by Markdown module"""
        return [self.converted(line) for line in lines]

    def converted(self, line:str) -> str:
        """Operate regex substitution of given line"""
        return self.CHECK_BOX_REGEX.sub(
            CheckBoxPreprocessor.checkbox_object,
            line
        )


    @staticmethod
    def checkbox_object(obj):
        """The core implementation, replacing a found [ ] expression
        by the HTML code calling for font awesome

        """
        chars = obj.groups()[0]
        size = 'fa-stack-1x'  # inital icon size (NB: necessary, can't be '')
        reversion = False  # True: inverse black and white
        icons = []
        for char in chars:
            if char in '12345':
                if char in '12345':
                    size = 'fa-stack-{}x'.format(char)
            elif char == '!':
                size = 'fa-stack-lg'
            elif char == '?':
                reversion = not reversion
            else:  # char is something to draw
                is_large = char.isupper() and char.upper() != char.lower()
                icons.append(CheckBoxPreprocessor.TEMPLATE_ICON.format(
                    ' fa-' + CheckBoxPreprocessor.ICONS[char.lower()],
                    ' fa-stack-lg' if is_large else (' ' + size),
                    ' fa-reverse' if reversion else ''
                ))
        if len(icons) == 1:
            return re.sub('-stack', '', icons[0])
        else:
            stack_size, last_char = 'fa-1x', chars[-1]
            if last_char == '!':
                stack_size = 'fa-large'
            elif last_char in '12345':
                stack_size = 'fa-{}x'.format(last_char)
            return CheckBoxPreprocessor.TEMPLATE_SPAN.format(
                stack_size,
            ''.join(icons)
        )
