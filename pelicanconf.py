#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Josh Montague'
SITENAME = u'clever title'
SITEURL = 'http://joshmontague.com'
MINI_BIO = u'I type into colored screens all day. Mostly about social data, mostly in Python.'
TIMEZONE = 'US/Mountain'
DEFAULT_LANG = u'en'

THEME = 'notmyidea'

ARTICLE_URL= 'posts/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = (
            ('Github', 'https://github.com/jrmontag'),
            ('Twitter', 'https://twitter.com/jrmontag'),
            ('LinkedIn', 'https://linkedin.com/in/joshuamontague'),
        )

GOOGLE_ANALYTICS = 'UA-XXXX-YYYY'
DISQUS_SITENAME = ''


# swap out of FILES_TO_COPY, re:
# https://github.com/getpelican/pelican/blob/master/docs/settings.rst#path-metadata 
PATH = '/Users/jrm/blog/src/content'
STATIC_PATHS = [
    'CNAME',
                ]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
