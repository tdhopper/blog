Title: Weekend Project: Build a Pelican-powered site on GitHub Pages 
Slug: pelican-on-github
Date: 2014-01-15 
Tags: python, pelican, git, weekend
Summary: Getting started using a GitHub project repository to host and serve the static content for a simple blog site written in Markdown, compiled and configured in Python. 

> Disclaimer: 
> This post got pretty long, especially for the first real post on this site. But by boiling down my very non-linear experience and putting this in writing, I hope that you could read through this and make it all work in an hour or so. Let me know how close that is to reality. 

For quick, get-up-and-running web publishing, there is [obviously](http://tumblr.com) [no](http://wordpress.com) [shortage](http://blogger.com) [of](http://medium.com) [platforms](http://ghost.org) [out](http://subtle.com) [there](http://typepad.com) to use; most have a free, hosted version, too (I'm sure there are a million other options I've never heard of). I've certainly started and neglected my share of these platforms (or had them disappear ... RIP [posterous](http://posterous.com)). 

But, I've been super excited learning things my new career\* and I was looking for an outlet for sharing (beyond the [140-character vignettes](http://twitter.com/jrmontag)). I was looking for a combination of things: balance between "get your hands dirty" and "don't get hung up on too many details", balance between "keep it lightweight" and "give me some features", and balance between "let me learn something new" and "keep it relevant". 

Ultimately, my love for Python won out and I went for a static [Pelican](https://pelican.readthedocs.org/)-based solution hosted via [GitHub Pages](http://pages.github.com/). From this combination of things I get:

- Python (the language with which I'm most familiar and love to use)

- Pelican (lightweight, fast, CLI tools for compiling and publishing, compose in Markdown) 

- git / GitHub (sweet sweet version control, plus open-source-y website)

While I'm still kicking the tires and figuring things out (I haven't even figured out how to change the theme yet), so far it's been fun to explore. There are some components that are still new to me, so I'm learning as I go. This edition of [Weekend Project](http://joshmontague.com/tag/weekend.html) is just about getting the pieces up and running - better understanding will hopefully come down the road.

\*Another good topic to write about in the future. 

---

I kicked this project off by reading two great posts by Martin Brochhaus ([newer](http://martinbrochhaus.com/pelican2.html), [older](http://martinbrochhaus.com/pelican.html)), but had to supplement those with various official docs along the way when I was in unfamiliar territory (which was approximately all of the time). I think I also had to add in a few tweaks for things that have changed since those posts were written. You could get most of this by just reading his posts (and I recommend clicking through), but I wanted the experience of writing it out. I've tried to include the most relevant extra links inline below where they were helpful to me - let me know if I missed something super useful.


# Local Python setup 

Let's install some packages. I'm using [`virtualenv`](https://pypi.python.org/pypi/virtualenv) to choose a specific Python interpreter and maintain an isolated set of packages relevant to this project. I'm also using [`virtualenvwrapper`](http://virtualenvwrapper.readthedocs.org/en/latest/) which is a wrapper for `virtualenv` that simplifies the API and makes it a little more friendly to use. Source `virtualenvwrapper.sh` and let it set things up with defaults (if you want to override the defaults, open the script and see what environment variables to set before you source the file). 

    :::bash
    sudo pip install virtualenv
    sudo pip install virtualenvwrapper
    # optionally export the correct environment vars used in the shell script 
    #   (if you want to override the defaults)
    . /usr/local/bin/virtualenvwrapper.sh

(Aside: through the process of setting up this project, I'm starting to finally grok `virtualenv`, and I suspect that `pip` (via e.g. `easy_install`), `virtualenv`, and `virtualenvwrapper` are among a small number of python packages that should ever be `sudo` installed, system-wide.) 

Create a new virtualenv (named 'blogging', for example) with a path to your interpreter (e.g. the result of `which python` or whichever installation you'd like to use), and `pip install` the relevant packages into that virtualenv (feel free to steal my [requirements.txt](https://github.com/jrmontag/blog/blob/master/requirements.txt) and run `pip install -r requirements.txt`). These packages will also install a bunch of others as dependencies.

    :::bash
    mkvirtualenv -p /path/to/.../python2.7 blogging     # for example
    pip install -r /path/to/.../requirements.txt
    # optionally check the currently-installed packages -- a handy cmd to know
    #   (this is like 'pip freeze' for the active virtualenv) 
    lssitepackages  

At the time of writing, I'm using Python 2.7.6 for this environment. A couple of other `virtualenvwrapper` commands that you'll want to know: 

    :::bash
    workon              # list the existing virtualenvs (also visible at ~/.virtualenv) 
    workon your_env     # enter the your_env virtualenv (prompt will change) 
    deactivate          # exit current virtualenv, return to system environment 

# Local project setup
This part is pretty subjective. Ultimately, we're going to have a git repository involved, but I'm actually keeping it above the root of my project tree for now. I have a `blog` directory at the bottom level and am planning to keep e.g. icon and theme directories in there, too. Soon, we'll create a git repository in the `src` directory to hold our content. First, use the handy Pelican [quickstart](https://pelican.readthedocs.org/en/3.2/getting_started.html#kickstart-your-site) command to set up the rest of the project structure:

    :::bash
    mkdir -p ~/blog/src
    cd ~/blog/src
    workon blogging     # or whatever you named your env (and if you aren't already in it)
    pelican-quickstart

Don't worry too much about the questions - I just hit enter for all of them to use the default settings. While still in the `src` directory, initialize a new git repository (`git init`) and create a `.gitignore` file with the lines below. We're excluding the compiled, swap, and output (mostly html and CSS) files. The content of `output/` will end up in our `gh-pages` branch (more on this shortly). 

    :::bash
    # add these to your .gitignore
    *.pyc
    *.swp
    *.pid       # this gets created by the develop_server.sh script
    output/ 

Let's sync the repo before we move on. Create a new project repository on GitHub, and skip the "Initialize this repository with a README" part. Grab the ssh address and bring it over to your new local repo. Set the upstream remote / master and add all your new content: 

    :::bash
    # assuming you've created the new-repo repository on github
    git add -A
    git commit -m"initial commit" 
    git remote add origin new-repo_ssh-address
    git push -u origin master

If that went well, you can cruise over the repo on GitHub and make sure all your files are there (and hopefully no `output/` directory because we included it in the `.gitignore`).  

Time to write your first post. Our articles are going in the `src/content/` directory. Pelican supports both [reStructuredText and Markdown](http://docs.getpelican.com/en/3.3.0/getting_started.html#file-metadata). The article syntax is different for the two filetypes, so when you pick one, check that link for the proper headings. If you want to just get started using Markdown, then create a simple new file like the one below.

    :::bash
    # create a file called hello-world.md in src/content/ 
    #   with something like the text below... 
    Tite: Hello World!
    Date: 2014-01-01
    Tags: pelican
    Slug: hello-world
    Author: Clark Kent
    Summary: In which the author writes their first blog post. 
 
    We're blogging with Pelican!

Now that you have some content, time to let Pelican do it's thing. The `pelican-quickstart` process should have created a Makefile in your `src` directory with some helpful commands for blog development. One of those is labeled `devserver` and it lets you view the current state of your `content` directory, locally at port 8000. You can look through what `make devserver` does (it calls the `develop_server.sh` shell script, which in turn calls on Pelican...) or just use it for now and understand it later. 

If all went as planned, you should be able to point a browser to `http://localhost:8000/` and see your new blog, live and kicking. Well, live in the only-exists-on-your-machine-while-devserver-is-running kind of way. But it's a start. For now, kill the local devserver process (cntl-C, followed by `./develop_server.sh stop` because cntl-C seemingly doesn't fully kill the process), and let's put this content somewhere where others can see it. 
 

# GitHub Pages setup

GitHub is amazingly powerful for a host of reasons. One of those is the ability to set up a low-... actually a basically zero-overhead website to display your projects via [GitHub Pages](http://pages.github.com/). A couple of stellar examples are the docs for [Jekyll](http://jekyllrb.com/) - a static website generator similar to Pelican but in Ruby - and Cam Davidson-Pilon's [Probabilistic Programming book](http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/). These are also great examples of having your content served through a custom domain (Jekyll) or from the default GitHub address of your project (Probabilistic...). [Tangent: I'm working through Davidson-Pilon's book right now and I highly recommend it if you're into that sort of thing.] 

For now, we'll use the latter and return to talk about custom domain names another time. To serve static content from a GitHub repo, you need a `gh-pages` branch as part of your project repo. If you're a git wizard and are already adept at managing branches, this may seem anticlimactic but we can use a [really handy script](https://github.com/davisp/ghp-import) that manages the `gh-pages` branch for us. To quote the docs:

>This saves me from even having to think about the branch and everything becomes magical.
>
>This is what `ghp-import` was written for.

If you used the `requirements.txt` file from my project when setting up your virtualenv, you should already have `ghp-import` installed (but recall that you can also check with `lssitepackages`). The `pelican-quickstart` command should have also added a `make github` portion to the Makefile. The pieces are falling into place like magic. The final step:

    :::bash
    make github

That's it. That make command actually does quite a lot, so definitely dig through the sequence of events there, but not right now. Right now, you should do two things: first, check that your repo has a new branch called `gh-pages` and then check that you can go to `https://your-user-name.github.io/new-repo-name`. (I'll totally understand if you do the second part first.) 

With luck (and minimal misleading mistakes on my part), you are well on your way. I've got a few other helpful upgrades to the base setup and will try to share any other future upgrades that might be helpful, too. Until then, happy blogging with your new GitHub Pages-hosted Pelican site. 


