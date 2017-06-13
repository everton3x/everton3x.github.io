#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Everton da Rosa'
SITENAME = 'Everton da Rosa'
SITEURL = 'https://everton3x.github.io'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Contabilidade Pública', 'https://everton3x.github.io/contabilidadepublica'))

# Social widget
SOCIAL = (('Facebook', 'https://facebook.com/everton3x'),
          ('Github', 'https://github.com/everton3x'),
          ('twitter', 'https://twitter.com/everton3x'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# theme
THEME = 'pelican-blue'
SIDEBAR_DIGEST = 'Contador de profissão e Programador de coração'
FAVICON = 'favicon.ico'
DISPLAY_PAGES_ON_MENU = True
TWITTER_USERNAME = 'everton3x'
MENUITEMS = (('Home', SITEURL),
             ('Sobre', '#'),)
LINKS = (('Link 1', '#'),
         ('Link 2', '#'),)
