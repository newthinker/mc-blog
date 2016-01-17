#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michael Cho'
SITENAME = u"Michael's blog"
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
    'zh_CN': '%Y-%m-%d %H:%M:%S',
}
DEFAULT_DATE_FORMAT = '%Y/%m/%d %H:%M:%S %a'
DEFAULT_DATE = 'fs'  # use filesystem's mtime
LOCALE = ('zh_CN.utf8',)
DEFAULT_LANG = u'zh_CN'

# licence 
CC_LICENSE = 'by-nc-sa'

## theme settings
THEME = '/mc/virtualenv/mc-blog/blog/themes/pelican-bootstrap3'
#BANNER = '/mc/virtualenv/mc-blog/blog/themes/pictures/banner1.jpg'
#BANNER_SUBTITLE = 'ZONE FOR CHO'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

## siderbar
# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/newthinker'),
	  ('twitter', 'https://twitter.com/zone4cho'),)

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git', '.gitignore']

# github
GITHUB_USER = 'newthinker'

# static files
STATIC_PATHS = [
    'images',
    'extra',
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

DEFAULT_PAGINATION = 10

# article path
PATH = '/mc/virtualenv/mc-blog/blog/content'
ARTICLE_PATHS = ['posts']

# URL settings
SLUGIFY_SOURCE = 'basename'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
