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
    ("About", "/pages/about.html"),
    ("Contact", "/pages/contact.html"),
    ("Rules", "/pages/rules.html"),
    ("Events", "/pages/events.html"),
    ("Shop", "https://87653163.shop.strato.de/")
)

# Pages
DISPLAY_PAGES_ON_MENU = True
CATEGORYS_SHOWN = False
TAGCLOUD_SHOWN = False

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
