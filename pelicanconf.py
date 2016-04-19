#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Josh Montague'
SITENAME = u'lab notebook'
SITEURL = 'http://joshmontague.com'
#SITEURL = 'http://jrmontag.github.io/blog'
MINI_BIO = u'I type into colored screens all day. Mostly about data, often in Python.'
TIMEZONE = 'US/Mountain'
DEFAULT_LANG = u'en'

# themes
#THEME = 'notmyidea'
THEME = 'pure-single'

# articles
ARTICLE_URL= 'posts/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}/index.html'

# pages
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
DISPLAY_PAGES_ON_MENU = True
PAGE_PATHS = ['pages']

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_CATEGORIES_ON_MENU = True

# Blogroll
LINKS =  ()

# from pure readme
COVER_IMG_URL = 'https://db.tt/EZ8f7qwr'
PROFILE_IMAGE_URL = 'http://2.gravatar.com/avatar/357be3e0935e653ba5cdae493f3dfcaf'
TAGLINE = 'thoughts and notes'

# social widgets (theme-specific)
if THEME == 'notmyidea':
    SOCIAL = ( 
            ('Github', 'https://github.com/jrmontag')
            , ('Twitter', 'https://twitter.com/jrmontag')
            , ('LinkedIn', 'https://linkedin.com/in/joshuamontague')
        )
elif THEME == 'pure-single':
    SOCIAL = (
            ('github', 'https://github.com/jrmontag')
            , ('twitter-square', 'https://twitter.com/jrmontag')
            , ('linkedin', 'https://linkedin.com/in/joshuamontague')
#            , ('rss', '/feeds/all.rss.xml')
        )
else:
    SOCIAL = (
        )


## swap out of FILES_TO_COPY, re:
## https://github.com/getpelican/pelican/blob/master/docs/settings.rst#path-metadata 
#FILES_TO_COPY = (
#        ('extra/CNAME', 'CNAME')
#        , ('extra/favicon.ico', 'favicon.ico')
#    )

# configure the filepath appropriately for the system we're on
# old MB
#PATH = '/Users/jrm/blog/src/content'
# MBP
PATH = '/Users/jmontague/blog/src/content'

STATIC_PATHS = [ 
                'extra',
                'images' 
                ]

# specify the desired output location of some files in the 'extra' dev dir
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'}, 
    'extra/favicon.ico': {'path': 'favicon.ico'}, 
    'extra/404.html': {'path': '404.html'},
    'extra/custom.css': {'path': 'theme/css/custom.css'} 
    }

# keep pelican from freaking out over pre-formed html 
READERS = {"html": None}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
