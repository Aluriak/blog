#!/usr/bin/python3
"""Wrapper generating an article for the website."""
import os
import re
import datetime
from functools import partial


KNOWN_TAGS = (
    'python', 'tools', 'language', 'graph', 'bioinformatic', 'meta', 'bio',
    'env', 'c/c++', 'rdf', 'opinion', 'stdlib', 'space'
)
KNOWN_LANGS = (('english', 'en'), ('français', 'fr'), ('lojban', 'lj'))
DEFAULT_LANG = KNOWN_LANGS[0][0]
DEFAULT_AUTHOR = 'Lucas Bourneuf'

REGEX_SLUG = r'[a-zA-Z0-9-]'  # only characters allowed in URL of articles

TEMPLATE_FILENAME = 'content/{}_{}.mkd'
TEMPLATE_CONTENT = """Title: {}
Date: {}
Modified: {}
Tags: {}
Authors: {}
Summary: {}
Slug: {}
lang: {}
translation: {}
status: draft

# First title

::: Python
    print('Here is Python !')


"""


def language_shortcut(lang, languages=KNOWN_LANGS):
    """Get the shortcut from given (fullname, shortname) list of language.

    >>>language_shortcut('angleesh') is None
    True
    >>>language_shortcut('english')
    'en'
    >>>language_shortcut('lj')
    'lj'

    """
    for full, short in languages:
        if lang in (full, short):
            return short
    return None

def human_bool(string):
    return string.strip().lower() in 'yYoOjJ1'

def human_words(string, expecteds):
    for word in string.strip().split(','):
        word = word.strip().lower()
        if word not in expecteds:
            print("WARNING: word '" + word + "' is unexpected."
                  "It will be added normally, but you have to modify"
                  " it or add it to known words.")
        yield word
# specialize the function for specific use cases
human_tags = partial(human_words, expecteds=KNOWN_TAGS)

def human_lang(string):
    for names in KNOWN_LANGS:
        if string.lower() in names:
            return names[0]
    print('WARNING: non valid language. DEFAULT_LANG is used.')
    return DEFAULT_LANG


def generated(title, tags, *, lang=DEFAULT_LANG, date=None,
              is_translation=False, authors=DEFAULT_AUTHOR, summary=''):
    """Write in ./content/ directory a file containing the markdown formatted
    squelleton for the given article."""
    if date is None:
        date = datetime.datetime.utcnow().strftime('%Y-%m-%d')
    slug = ''.join(c for c in title.strip().lower().replace(' ', '-')
                   if re.fullmatch(REGEX_SLUG, c))
    content = TEMPLATE_CONTENT.format(
        title, date, date, tags, authors, summary,
        slug, lang, 'true' if is_translation else 'false'
    )

    # Write it to the file
    filename = TEMPLATE_FILENAME.format(slug, language_shortcut(lang))
    assert not os.path.exists(filename)
    with open(filename, 'w') as fd:
        fd.write(content)
    return


generated(
    title=input('Title: '),
    tags=', '.join(human_tags(input('TAGS: {}\ntags: '.format(', '.join(KNOWN_TAGS))))),
    summary=input('summary: '),
    lang=human_lang(input('lang[en/fr/lj]: ')),
    is_translation = human_bool(input('translation [y/n]: ')),
)
