Title: From plain text to JSON with <code>jq</code>
Slug: create-json-with-jq
Date: 2014-09-28
Category: shortread
Tags: bash, shell, jq, json, tools 
Summary: Sometimes using tools differently than intended has fantastic results. Creating nested JSON from a tab- and newline-delimited text file. 


Most data in my work world is [JSON](http://www.json.org/), and so I use a lot of tools designed for that format. For example, we maintain (and use, all the time) [an activity parser](https://pypi.python.org/pypi/gnacs/) that is designed for Gnip's [Activity Stream](http://en.wikipedia.org/wiki/Activity_Streams_(format)) data format from a half dozen different platforms. It handles all the assorted messages you might get from the API, and lets you pick and choose the output, among other things. 

A relatively new arrow in my quiver of tools at work is [``jq``, a fast and easy command-line JSON parser](http://stedolan.github.io/jq/). This particular quote on the website is the best summary:

> ``jq`` is like ``sed`` for JSON data – you can use it to slice and filter and map and transform structured data with the same ease that ``sed``, ``awk``, ``grep`` and friends let you play with text.  

I recently [wrote on an article](http://support.gnip.com/articles/data-and-rule-management-with-jq.html) for our support site about using ``jq``; a kind of "tips and tricks with ``jq``". This gave me a great opportunity to experiment with something I'd been curious about: can ``jq`` be used to *create* JSON structures?  

Spoiler alert: the answer is yes! 

You can [click over there if you'd like to read the full article](http://support.gnip.com/articles/data-and-rule-management-with-jq.html), but I'll add the punch line here. With a combination of ``split``, ``map``, the right command-line arguments, and an alias, I now use this regularly:

    :::shell
    $ cat rules.txt     # tab-separated columns
    dog lang:en	tag:dogs:english
    cat sample:10	tag:cats:0.1
    from:gnip	tag:user:gnip

    $ jqrules rules.txt
    {
      "rules": [
        {
          "value": "dog lang:en",
          "tag": "tag:dogs:english"
        },
        {
          "value": "cat sample:10",
          "tag": "tag:cats:0.1"
        },
        {
          "value": "from:gnip",
          "tag": "tag:user:gnip"
        }
      ]
    }

If you skim through [the documentation](http://stedolan.github.io/jq/manual/), it's clear that ``jq`` can do a ton of awesome things; every time I learn a new one, it's a great boost in productivity. Happy JSON parsing (and, now, creating)!

