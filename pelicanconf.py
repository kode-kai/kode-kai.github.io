#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Kode Kai'
SITENAME = 'Kode Kai'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
        ('YouTube', 'https://www.youtube.com/channel/UCEOGKsAcIpVGxgdCTq7z-Zg'),
        ('Twitch', 'https://twitch.tv/kode_kai'),
        ('Twitter', 'https://twitter.com/kode_kai'),
        ('GitHub', 'https://github.com/kode-kai'),
        ('Facebook', 'https://www.facebook.com/kodekaishow/'),
    )

SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'clean-blog'

COLOR_YELLOW = '#F8E71C'
COLOR_RED = '#B50218'

HEADER_COLOR = '#F8E71C'