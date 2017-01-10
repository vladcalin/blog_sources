#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Vlad Calin'
SITENAME = 'Vlad\'s blog'
SITEURL = ''
SITELOGO = "/images/profile.jpg"
SITETITLE = "Vlad Călin"
SITESUBTITLE = "Software developer - writing Python code for money"
SITEDESCRIPTION = "When every morning starts with a coffee and a hello world"

ROBOTS = 'index, follow'
COPYRIGHT_YEAR = 2016

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True

# Blogroll
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)
LINKS = ()


# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/calinstefanvlad'),
          ('github', 'https://github.com/vladcalin'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "Flex"
STATIC_PATHS = ["images"]
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}