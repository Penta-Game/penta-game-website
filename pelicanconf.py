#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Cobalt'
SITENAME = 'Pentagame'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

THEME = "theme"

USE_FOLDER_AS_CATEGORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Menu Items used in navbar

MENUITEMS = (
    ("Rules", "/pages/rules.html"),
    ("About", "/pages/about.html"),
    ("Events", "/pages/events.html"),
    ("Contact", "/pages/contact.html"),
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
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
