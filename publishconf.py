import sys
sys.path.append('.')
from pelicanconf import *  # get all data


# adresses complètes : le flux atom et le sitemap sont lus hors du site
SITEURL = SERVERURL + '/blog'
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = False
FEED_ATOM = 'feeds/atom.xml'
