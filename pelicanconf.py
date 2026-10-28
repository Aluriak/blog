import sys
sys.path.append('.')


################################################################################
#                           GENERAL DATA
################################################################################
AUTHOR = 'lucas bourneuf'
SITENAME = "lucas/blog"
SERVERURL = 'https://lucas.bourneuf.net'
SITEURL = '/blog'
LANDING_URL = SERVERURL + '/landing/'  # lien « menu » de l'en-tête (la landing)

PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'
# langue des articles (Lang: français…) → code pour <html lang> (cf. create_content.py)
LANG_CODES = {'français': 'fr', 'english': 'en', 'lojban': 'jbo', 'lj': 'jbo'}
DEFAULT_PAGINATION = None

READERS = {'htm': None}  # htm pages are not processed, but html are.
STATIC_PATHS = ['images/']

# Articles default metadata
DEFAULT_METADATA = {
        'status': 'draft',
}

DEFAULT_DATE_FORMAT = '%d/%m/%Y'


################################################################################
#                               THEME
################################################################################
THEME = 'mythemes/vert-sur-noir'


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


PLUGINS += [
    'chargement_differe',  # images chargées à l'approche de l'écran (loading="lazy")
    'mail_image',  # adresse MAIL dessinée dans mail.png
]

TAG_CLOUD_STEPS = 2  # number of different size
TAG_CLOUD_MAX_ITEMS = 10
TAG_CLOUD_SORTING = 'random'
TAG_CLOUD_BADGE = True

LICENCE = 'GPLv3'  # affichée dans le pied de page
LICENCE_URL = 'https://www.gnu.org/licenses/gpl-3.0.html'



################################################################################
#                           LINKS & FEEDS
################################################################################
# Blogroll:   (icône font awesome 6, nom affiché, lien)
# icône : « house » (style solid), ou avec le style : « brands github », « regular square »
# lien : une adresse, ou MAIL pour afficher l'adresse en image (mail.png, plugin mail_image),
# que les robots qui cherchent des adresses dans le HTML ne voient pas
MAIL = ('lucas.bourneuf', 'laposte.net')
BLOG_LINKS = 'blog', 'bars', (
    ('house',      'home',    '{}'.format(SITEURL)),
    ('table-list', 'archive', '{}/archives.html'.format(SITEURL)),
    ('link',       'links',   '{}/links'.format(SERVERURL)),
)
LINKS = 'links', 'arrow-up-right-from-square', (
    ('brands github',   'github',   'https://github.com/aluriak'),
    ('brands mastodon', 'mastodon', 'https://mamot.fr/@aluriak'),
    ('brands keybase',  'keybase',  'https://keybase.io/aluriak'),
    ('cube',            'IPNS',     'https://bourneuf.net/ipns/Qmd4up4kjr8TNWc4rx6r4bFwpe6TJQjVVmfwtiv4q3FSPx'),
    ('envelope',        'mail',     MAIL),
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
#                           DIVERS
################################################################################
LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = True
RELATIVE_URLS = True  # en local ; adresses complètes pour la publication (publishconf.py)
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', '404']
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
