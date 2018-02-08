# -*- coding: utf-8 -*-

import feedparser


ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
entries = ny['entries']
