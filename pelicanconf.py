#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'P. Pérez'
SITENAME = u'i+d en física médica'
SITETITLE = AUTHOR
SITESUBTITLE = SITENAME
SITEDESCRIPTION = u'Sitio web de P. Pérez en web oficial de la Facultad de Matemática, Astronomía, Física y Computación de la UNC.'

# Ver si hay que corregir esto cuando sea para post
#SITEURL = 'htttp://famaf.unc.edu.ar/~pperez1'
#SITELOGO = SITEURL + '/images/profile.png'
SITEURL = 'http://www.famaf.unc.edu.ar/~pperez1/'
SITELOGO = SITEURL + 'images/profile.png'

THEME = u"../pelican-themes/Flex"
PATH = 'content'
STATIC_PATHS = ['images', 'pdfs', 'pages', 'blog']
ARTICLE_PATHS = ['blog']
PAGE_PATHS = ['pages']
TIMEZONE = 'America/Argentina/Cordoba'
DEFAULT_LANG = u'es'

#INDEX_SAVE_AS = 'index.html'
#PAGE_SAVE_AS = '{slug}.html'
#PAGE_URL = '{slug}.html'

#PAGE_ORDER_BY = 'slug'

#DISPLAY_PAGES_ON_MENU = False
#MAIN_MENU = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Configuracion propia
USE_FOLDER_AS_CATEGORY = False
DISPLAY_SOCIAL_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git']
ARTICLE_PATHS = [] # dirección dentro de content/ donde van a ir los argículos
#TYPOGRIFY = True
