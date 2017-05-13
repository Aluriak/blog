from __future__ import unicode_literals
import sys
sys.path.append('.')
from pelicanconf import *  # get all data



# override pelicanconfig
DELETE_OUTPUT_DIRECTORY = False
FEED_ATOM = 'feeds/atom.xml'
# RELATIVE_URLS = False
PIWIK = True  # not used as url holder, but uniquely as enable/disable piwik
