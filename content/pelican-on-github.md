Title: Weekend Project: Build a Pelican-powered site on GitHub Pages 
Slug: pelican-on-github
Date: 2014-01-04 
Tags: python, pelican, github, weekend
Summary: Use a GitHub project repository to host the static HTML and CSS for simple website/blog written in Markdown, compiled and configured in Python. 


For quick, get-up-and-running web publishing, there is [obviously](http://tumblr.com) [no](http://wordpress.com) [shortage](http://blogger.com) [of](http://medium.com) [platforms](http://ghost.org) [out](http://subtle.com) [there](http://typepad.com) to use; most have a free, hosted version, too (I'm sure there are a million other options I've never heard of). I've certainly started and neglected my share of these platforms (or had them disappear ... RIP [posterous](http://posterous.com)). 

In my latest endeavor to share things -- driven by excitement about my new work universe -- I was looking for a combination of things: balance between "get your hands dirty" and "don't get hung up on too many details", balance between "keep it lightweight" and "give me some features", and balance between "let me learn something new" and "keep it relevant". 

Ultimately, my love for Python won out (over e.g. [Jekyll](http://jekyllrb.com/)) and I went for a Pelican-based solution hosted by GitHub Pages. From this combination of things I get:

- Python (the language with which I'm most familiar and love to use)

- Pelican (lightweight, static, CLI tools for compiling and publishing, compose in Markdown) 

- git / GitHub (sweet sweet version control, plus 'open-source-y' website code)

I've also just found it plain *fun* with this setup. It's still in its infancy (I haven't even figured out how to change the theme yet), but so far it's been really fun to explore. There are some components that are still new to me, so I'm learning as I go. This edition of Weekend Project is just about getting the pieces up and running -- better understanding will hopefully come down the road.

---

I kicked this project off by reading two great posts by Martin Brochhaus ([newer](http://martinbrochhaus.com/pelican2.html), [older](http://martinbrochhaus.com/pelican.html)), and then had to supplement those with various official docs along the way when I was in unfamiliar territory (which was approximately all of the time). I've tried to include the most relevant links inline below where they were helpful to me - let me know if I missed something super useful.


# Local Python setup 

Let's install some packages. I'm using [`virtualenv`](https://pypi.python.org/pypi/virtualenv) to choose the interpreter and maintain an isolated set of packages relevant to this project. I'm also using [`virtualenvwrapper`](http://virtualenvwrapper.readthedocs.org/en/latest/) which is a wrapper for `virtualenv` that simplifies the API and makes it a little more friendly to use. Source `virtualenvwrapper` and let it set things up with defaults (if you want to override the defaults, open the script and see what environment variables to set before you source the file). 

    :::bash
    sudo pip install virtualenv
    sudo pip install virtualenvwrapper
    # optionally export the environment vars used in the shell script 
    . /usr/local/bin/virtualenvwrapper.sh

(Aside: As a result of this project, I'm starting to finally **get** `virtualenv`, and I suspect that `pip` (via e.g. `easy_install`), `virtualenv`, and `virtualenvwrapper` are among a small number of python packages that should ever be `sudo` installed.) 

Create a new virtualenv (named 'blogging', for example) with a path to your interpreter (e.g. the result of `which python` or whichever installation you'd like to use), and `pip install` the relevant packages into that virtualenv (feel free to steal my [requirements.txt](https://github.com/jrmontag/jrmontag-blog/blob/master/requirements.txt) or fork the [whole repo](https://github.com/jrmontag/jrmontag-blog)). These packages will also install a bunch of others as dependencies.

    :::bash
    mkvirtualenv -p /path/to/.../python2.7 blogging     # for example
    pip install -r /path/to/.../requirements.txt
    lssitepackages  # optionally, check the currently-installed packages
    
# Local project setup

This part is pretty subjective. Ultimately, we're going to have a git repository involved, but I'm actually keeping it above the root of my project tree for now. I have a `blog` root directory and am planning to keep e.g. icon and theme directories in there, too. 

    :::bash
    mkdir -p ~/blog/src
    cd ~/blog/src






<!--
text

    :::
    blog
    |-- icons
    |-- plugins
    |-- themes
    |-- src
-->

