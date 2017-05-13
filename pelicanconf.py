#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
sys.path.append('.')


################################################################################
#                           GENERAL DATA
################################################################################
AUTHOR = 'lucas bourneuf'
SITENAME = "lucas/blog"
SERVERURL = 'https://lucas.bourneuf.net'
SITEURL = '/blog'

PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = None

STATIC_PATHS = ['images/']

# Articles default metadata
DEFAULT_METADATA = {
        'status': 'draft',
}

# date format (could be set by langage)
DEFAULT_DATE_FORMAT = '%d/%m/%Y'
# DATE_FORMATS = {
    # 'en': '%d/%m/%Y',
    # 'fr': '%d/%m/%Y',
    # 'lj': '%d/%m/%Y',
# }


PIWIK = False  # not used as url holder, but uniquely as enable/disable piwik


################################################################################
#                               THEMES
################################################################################
# theme names
THEME_SIMPLE = 'simple'
THEME_NMNLIST = 'nmnlist'
THEME_BOOTSTRAP = 'bootstrap2-dark'
THEME_FUU = 'fuu'

# paths
THEMES_PATH = 'themes/'
MY_THEMES_PATH = 'mythemes/'

# this is the one
# THEME = THEMES_PATH + THEME_BOOTSTRAP
THEME = MY_THEMES_PATH + THEME_BOOTSTRAP
# THEME = MY_THEMES_PATH + THEME_FUU
# THEME = MY_THEMES_PATH + THEME_NMNLIST

# themes config
if THEME_NMNLIST in THEME:
    HIDE_DATE = False


################################################################################
#                           MARKDOWN PLUGINS
################################################################################
# Markdown plugins
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'myplugins.checkbox:BoxExtension': {},
        'myplugins.separator:TitleSepExtension': {},
    }
}

# Markdown plugins setup
pass


################################################################################
#                           PELICAN PLUGINS
################################################################################
PLUGIN_LIQUID_TAG = [
    'liquid_tags.img',
    'liquid_tags.video',
    # 'liquid_tags.youtube',
    # 'liquid_tags.vimeo',
    # 'liquid_tags.include_code',
    # 'liquid_tags.notebook'
]

# Pelican plugins
PLUGIN_PATHS = ['./pelican-plugins', './myplugins']
PLUGINS = [
    # 'autopages',  # page for authors, tags and categories
    # 'post_stats',  # compute statistics on articles
    'random_article',  # provides a randomly choosen article link
    # 'global_license',  # provides a global constant, containing the license text
    'github_activity',  # dynamic access to github activity
    # 'backreftranslate',  # add is_translation_of attribute to translated articles
    'tag_cloud',  # tag cloud
    *PLUGIN_LIQUID_TAG,  # insert images, videos,… properly
    'section_number',
    'filetime_from_git',
    # 'render_math',

    # My plugins
]


# ACTIVATED PLUGINS DATA
GITHUB_URL = 'https://github.com/aluriak.atom'
GITHUB_ACTIVITY_FEED = 'https://github.com/aluriak.atom'
GITHUB_ACTIVITY_MAX_ENTRIES = 5
RANDOM = 'random.html'  # random_article: name of the generated HTML page
TAG_CLOUD_STEPS = 2  # number of different size
TAG_CLOUD_MAX_ITEMS = 10
TAG_CLOUD_SORTING = 'random'
TAG_CLOUD_BADGE = True

# DEACTIVATED PLUGINS DATA
LICENCE = 'WTFPL'  # LICENCE text, globally available



################################################################################
#                           LINKS & FEEDS
################################################################################
# Blogroll:   (font awesome icon, diplayed name, link)
BLOG_LINKS = 'blog', 'bars', (
    ('home',    'home',    '{}'.format(SITEURL)),
    ('th-list', 'archive', '{}/archives.html'.format(SITEURL)),
    ('link',    'links',   '{}/links'.format(SERVERURL)),
)
LINKS = 'links', 'external-link', (
    ('github',  'github',  'https://github.com/aluriak'),
    ('twitter', 'twitter', 'https://twitter.com/@aluriak'),
    ('key',     'keybase', 'https://keybase.io/aluriak'),
    ('cube',    'IPNS',    'https://bourneuf.net/ipns/Qmd4up4kjr8TNWc4rx6r4bFwpe6TJQjVVmfwtiv4q3FSPx')
    # ('stack-exchange',     'stackexchange', 'http://stackexchange.com/users/3696842/aluriak'),
    # ('windows',     'indexerror', 'http://indexerror.net/user/lucas'),
)
OUTER_WEB = 'outer web', 'wpexplorer', (
    ('users',  'pro-domo',  'https://pro-domo.ddns.net/blog'),
)


# FEED_ATOM = 'feeds/atom.xml'
# FEED_RSS = 'feeds/rss.xml'

ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_LANG_URL = '{slug}-{lang}.html'
DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
DRAFT_LANG_URL = 'drafts/{slug}.html'



################################################################################
#                           OTHER & WEIRD
################################################################################
LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = True
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
