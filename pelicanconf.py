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
LANDING_URL = SERVERURL + '/landing/'  # lien « autres outils » de l'en-tête

PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = None

READERS = {'htm': None}  # htm pages are not processed, but html are.
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




################################################################################
#                               THEMES
################################################################################
# theme names
THEME_SIMPLE = 'simple'
THEME_NMNLIST = 'nmnlist'
THEME_VERT = 'vert-sur-noir'
THEME_FUU = 'fuu'

# paths
THEMES_PATH = 'themes/'
MY_THEMES_PATH = 'mythemes/'

# this is the one
THEME = MY_THEMES_PATH + THEME_VERT
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
        'markdown.extensions.meta': {},  # metadata
        'markdown.extensions.abbr': {},  # allows abbreviations
        'markdown.extensions.toc': {'anchorlink': True},  # table of content
        'myplugins.checkbox:BoxExtension': {},  # fontawesome boxes
    }
}

# Markdown plugins setup
pass


################################################################################
#                           PELICAN PLUGINS
################################################################################
# Plugins : paquets pip pelican-* (voir requirements.txt), l'ancien dépôt pelican-plugins
# n'est plus maintenu. Plus disponibles : random_article, github_activity, section_number.
LIQUID_TAGS = ['img', 'video']  # insert images, videos,… properly
PLUGIN_PATHS = ['./myplugins']
PLUGINS = [
    'pelican.plugins.liquid_tags',
    'liquid_avant_html',  # balises liquid aussi dans les blocs HTML (<center>…), cf. myplugins
    'pelican.plugins.tag_cloud',  # tag cloud
    'pelican.plugins.sitemap',  # cf SITEMAP var
]


# ACTIVATED PLUGINS DATA
GITHUB_URL = 'https://github.com/aluriak.atom'
GITHUB_ACTIVITY_FEED = 'https://github.com/aluriak.atom'
GITHUB_ACTIVITY_MAX_ENTRIES = 5
RANDOM = 'random.html'  # random_article: name of the generated HTML page
SECTION_NUMBER_MAX = 5
TAG_CLOUD_STEPS = 2  # number of different size
TAG_CLOUD_MAX_ITEMS = 10
TAG_CLOUD_SORTING = 'random'
TAG_CLOUD_BADGE = True
TOC = {'TOC_HEADERS': '^h[1-4]', 'TOC_RUN': 'false'}

# DEACTIVATED PLUGINS DATA
LICENCE = 'WTFPL'  # LICENCE text, globally available



################################################################################
#                           LINKS & FEEDS
################################################################################
# Blogroll:   (icône font awesome 6, nom affiché, lien)
# icône : « house » (style solid), ou avec le style : « brands github », « regular square »
BLOG_LINKS = 'blog', 'bars', (
    ('house',      'home',    '{}'.format(SITEURL)),
    ('table-list', 'archive', '{}/archives.html'.format(SITEURL)),
    ('link',       'links',   '{}/links'.format(SERVERURL)),
)
LINKS = 'links', 'arrow-up-right-from-square', (
    ('brands github',   'github',   'https://github.com/aluriak'),
    ('brands twitter',  'twitter',  'https://twitter.com/@aluriak'),
    ('brands mastodon', 'mastodon', 'https://mamot.fr/@aluriak'),
    ('brands keybase',  'keybase',  'https://keybase.io/aluriak'),
    ('cube',            'IPNS',     'https://bourneuf.net/ipns/Qmd4up4kjr8TNWc4rx6r4bFwpe6TJQjVVmfwtiv4q3FSPx'),

    # ('brands stack-exchange', 'stackexchange', 'http://stackexchange.com/users/3696842/aluriak'),
    ('brands windows',  'indexerror', 'http://indexerror.net/user/lucas'),
    ('envelope',        'mail',       'mailto:{{firstname}}.{{lastname}}@laposte.net'),
)
OUTER_WEB = 'outer web', 'brands wpexplorer', (
    ('circle-user',  'pro-domo',  'https://pro-domo.ddns.net/blog'),
    ('circle-user',  'dridk',     'http://dridk.labsquare.org/'),
)


ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_LANG_URL = '{slug}.html'
ARTICLE_LANG_SAVE_AS = '{slug}.html'
DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
DRAFT_LANG_URL = 'drafts/{slug}.html'
DRAFT_LANG_SAVE_AS = 'drafts/{slug}.html'



################################################################################
#                           OTHER & WEIRD
################################################################################
LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = True
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
FEED_ATOM = 'feeds/atom.xml'
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'monthly',
        'pages': 'monthly'
    }
}
