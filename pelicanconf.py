#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michael Cho'
SITENAME = u"Michael's blog"
SITEURL = 'http://blog.zone4cho.me'

TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
    'zh_CN': '%Y-%m-%d %H:%M:%S',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_DATE = 'fs'  # use filesystem's mtime
LOCALE = ('zh_CN.utf8',)
DEFAULT_LANG = u'zh_CN'
FILENAME_METADATA = '(?P<slug>.*)'

# licence
CC_LICENSE = 'by-nc-sa'

## theme settings
THEME = './themes/niu-x2-sidebar'
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
SOCIAL = (
    ('github', 'https://github.com/newthinker'),
    ('twitter', 'https://twitter.com/zone4cho'))

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git', '.gitignore']

# github
GITHUB_USER = 'newthinker'

# static files
STATIC_PATHS = [
    'images',
    'extra',
    'pdfs'
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


JINJA_EXTENSIONS = [
    'jinja2.ext.ExprStmtExtension',
]

# plugin config
PLUGIN_PATHS = ['./plugins']
PLUGINS = [
    # 'gzip_cache',
    # 'pandoc_reader',
    # 'update_date',
    # 'extract_headings',
    # 'sitemap',
    # 'summary',
    # 'niux2_lazyload_helper',
    # 'niux2_hermit_player',
    # 'minify',
]
UPDATEDATE_MODE = 'metadata'
