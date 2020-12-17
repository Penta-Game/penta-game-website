#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Cobalt'
SITENAME = 'Pentagame'
SITEURL = 'https'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

THEME = "theme"

USE_FOLDER_AS_CATEGORY = True

# Plugins
PLUGINS = []

# article url settings
ARTICLE_PATHS = ["articles"]
ARTICLE_URL = "blog/{category}/{slug}/"
ARTICLE_SAVE_AS = "blog/{category}/{slug}/index.html"
ARTICLE_LANG_SAVE_AS = "blog/{category}/{slug}-{lang}/index.html"
ARTICLE_LANG_URL = "blog/{category}/{slug}-{lang}/"
DRAFT_URL = 'drafts/{slug}/index.html'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'
DEFAULT_METADATA = {"status": "published"}

# Category url settings
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

# Page url settings
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"
PAGE_LANG_URL = "pages/{lang}/{slug}/"
PAGE_LANG_SAVE_AS = "pages/{lang}/{slug}/index.html"

# Prefixes
PREFIXES = ["/pages/*", "/blog/*", "/category/*"]

# Menu Items used in navbar

MENUITEMS = (
    ("Rules", "/pages/rules/"),
    ("About", "/pages/about/"),
    ("Events", "/pages/events/"),
    ("Contact", "/pages/contact/"),
    ("Shop", "https://87653163.shop.strato.de/") 
)

# Pages
DISPLAY_PAGES_ON_MENU = True
CATEGORYS_SHOWN = False  # Due to WIP
TAGCLOUD_SHOWN = False  # Due to WIP
LINKS_SHOWN = False  # Due to WIP
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
