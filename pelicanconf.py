#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Josh Montague'
SITENAME = u'clever title'
SITEURL = 'http://joshmontague.com'
MINI_BIO = u'I move bits around all day. Mostly social data, mostly in Python.'

TIMEZONE = 'US/Mountain'

DEFAULT_LANG = u'en'

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

# CNAME
#FILES_TO_COPY = (( 'CNAME', 'CNAME'),
#                )
# edit to reflect https://github.com/mbrochh/mbrochh-blog/commit/979c74d368aa560efbfeb8125344e6226581484f
PATH = '/Users/jrm/blog/src/content'
STATIC_PATHS = [
    'CNAME',
                ]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
