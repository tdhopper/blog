Title: MNIST + <code>scikit-learn</code>
Slug: mnist-scikit-learn
Date: 2016-01-18
Category: longread 
Tags: python, ML, machine learning, scikit-learn, sklearn, MNIST, digits, supervised learning 
Summary: Python code and an approach to classifying the MNIST handwritten digits dataset with a 98+% accuracy for about $3 in infrastucture costs.  


*Update: There are a bunch of handy "next-step" pointers related to this work [in the corresponding reddit thread.](https://www.reddit.com/r/MachineLearning/comments/433pbm/using_pythons_scikitlearn_library_to_achieve_98/)* 

During the holidays, the work demand on my team tends to slow down a little while people are out or traveling for the holidays. For the second year, we held an intra-team team competition in the vein of [Kaggle competitions](https://www.kaggle.com/competitions). As in those competitions, entrants are given training data and labels, along with the test data on which to make predictions. The submitted predictions are scored and posted to the shared leaderboard (though our leaderboard is typically just a Google Spreadsheet).  

This competition was based on one of the canonical machine learning datasets, [the MNIST handwritten digits](https://en.wikipedia.org/wiki/MNIST_database). This data has [a wonderfully rich history](http://yann.lecun.com/exdb/mnist/), and has been a standard benchmark for classification approaches since the 1990s. The data is in the form of 60,000 training images that are grayscale (intensity levels from 0-255) with accompanying labels (integers 0-9), and 10,000 test images of the same format (but without the labels, of course). 

<center>
![Example MNIST digit]({filename}/images/mnist-2.png "28x28-pixel digit image")

An example digit (labeled as a 2) from the MNIST dataset.  
</center>

I was pretty surprised that with [the current release of ``scikit-learn``](http://scikit-learn.org/stable/install.html) (0.17 at the time of writing), a [c3.8xlarge EC2 instance](https://aws.amazon.com/ec2/instance-types/#c3), and about 1.5 hours of processing time, I could obtain above 98% accuracy on the test data (and win the competition). Based on just the infrastructure, I think this would cost about $3.[^3dollars] Pretty cool! This obviously ignores the value of my time, my previous experience, and the work it took to get to the final solution, but that's a much less quotable way to say it. 

<center>
<blockquote class="twitter-tweet" data-conversation="none" lang="en"><p lang="en" dir="ltr">Year two victory was even more narrow! Last year&#39;s prize was tastier, but this one will probably last longer 🚁😊 <a href="https://t.co/OZ39CShJfX">https://t.co/OZ39CShJfX</a></p>&mdash; Josh Montague (@jrmontag) <a href="https://twitter.com/jrmontag/status/686224933916037120">January 10, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>
 
I thought it would be fun to write down how I approached the problem, so here we go! 

First, some history. Last year, we built models to predict third-party predictions of Tweet text sentiment. This was, effectively, "modeling someone else's model." The first edition of the competition went well for me... 

<center>
<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">Our team had a kaggle-like competition for <a href="https://twitter.com/hashtag/hackweek?src=hash">#hackweek</a>. Narrow victory; totally worth the time invested. <a href="http://t.co/KsO0LmTMxt">pic.twitter.com/KsO0LmTMxt</a></p>&mdash; Josh Montague (@jrmontag) <a href="https://twitter.com/jrmontag/status/555054775620755456">January 13, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>

... so this year I felt some pressure as the incumbent. Further adding to the pressure, our whole team has come a long way in our machine learning and modeling abilities, and I think one of my principal advantages the first year was a familiarity with the [``scikit-learn`` library](http://scikit-learn.org/stable/). 

Unfortunately, I never got to write up my experience in the first competition because I was **embarassingly disorganized** in my approach. This haunted me for an entire year, so my goal for this year's edition (in addition to *winning*) was to strive for a more thoughtful, transparent, and reproducible approach from the very beginning. To be clear, I'm still not an expert in machine learning (this will become clear, shortly) and I figured I'd make some poor choices and mistakes along the way; but, at least this time I'd be more disciplined in my approach. 

# Overview 

So far, I've tended to think of approaching and solving modeling problems as working along two non-orthogonal axes (especially in machine learning): data/feature engineering, and model selection. Doing both well is the ideal scenario! Short of that, you should play to your strengths, right? Since my knowledge of the ``scikit-learn`` API is greater than my knowledge of robust data (feature) engineering, I opted to pursue a "start very wide and focus on the successes" approach to the problem. I would start by iteratively refining a set of models for higher accuracy, and then maybe combine them with some ensemble techniques. If or when I exhausted that path, I'd go back and spend more time on feature engineering.


# Approach

For the sake of following along, you can always [hop over to poke around in my code](https://github.com/jrmontag/mnist-sklearn). You could even follow the README instructions to build the whole thing while you're reading this article!

The data was handed to us in a binary format that I didn't fully understand.[^yan] But, we also got the included ``images.py`` script which illustrated how to read the data and printed cute ascii versions of the characters to the screen. This was enough code for me to modify and figure out how to unroll the ``numpy`` arrays for each image, combine them into a single array, and write that to disk. Now, instead of 60,000 28x28-pixel images, I had a 60,000-row matrix with 784 columns/features (the unrolled pixels). 

At this point, I fired up an [IPython notebook](http://jupyter.readthedocs.org/en/latest/) to interactively figure out how to chain together the file reads, model fits, cross-validation (with model accuracy visualization!), test data prediction, and submission file creation. The first model I always like to create is the ``DummyClassifier`` which basically ignores your training data! Not only is it fast, it's a great way to set a baseline score to ensure you don't make a submission that's *worse than random guessing*. 

<center>
<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">classifier seems to be working as designed. <a href="https://twitter.com/hashtag/saturdaymorning?src=hash">#saturdaymorning</a> <a href="https://t.co/6zbS5FZqct">pic.twitter.com/6zbS5FZqct</a></p>&mdash; Josh Montague (@jrmontag) <a href="https://twitter.com/jrmontag/status/678314414425018368">December 19, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
</center> 

With this notebook setup, I experimented with a handful of models to get some scores on the board: random guessing, a linear SVM, and adding scaling into a pipeline. Then, before getting too far into it (like last year!), I started pulling things out into a more programmatic  approach. 

Recognizing that the provided dataset was quite small, I presumed I wouldn't be bottlenecked by memory constraints. Rather, I decided I could move fastest in exploration by parallelizing the CPU-intensive model training steps. Since many of the ``scikit-learn`` estimators already have parallelization built in (all hail ``n_jobs=-1`` 🙌), I tried to design a workflow that would let me run many experiments in parallel, try not to run them all at exactly the same time, and then let the operating system deal with process management.

To do this, I used a bash script (``launch-processes.bash``) that manages things like paths, filenames, process timing (what to start and when), and command-line options. This script is essentially just a wrapper that executes the central Python script (``build-model.py``) with varying command-line options. The Python script is pretty generic: it reads data, fits a ``scikit-learn`` estimator, and either reports on the cross-validation accuracy (through logging and figure generation), or creates a submission file for the leaderboard based on the test data. 

Since the ``scikit-learn`` API is very consistently designed, I abstracted away the specific details of the model so I could specify them at run-time (through a command-line argument). Thinking about execution in this way let me use a numeric mapping to specify the models, and define those in a separate module (``models.py``). By using integers for the mapping, I could write a simple for loop (in bash) over the range of integers (models) I wanted to run. 

# Procedure

All of the models are defined [in terms of ``Pipeline``s](http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html), so they can all be treated like an arbitrary estimator in the Python script: calling ``.transform()``, ``fit()``, or ``.predict()`` just works as you'd expect it to. This is an amazing feature of the ``scikit-learn`` library that makes it super easy to drop different estimators into an existing workflow. And that is precisely what I did! I worked through these steps, in about this order: 

- score default instances of nearly every classifier in the ``scikit-learn`` library, with and without feature scaling. This gets you up to ``expt_23`` in ``models.py``.
- choose the top three, best-scoring models [k-nearest neighbors, rbf-kernel SVM (with feature scaling), and random forest (with feature scaling)], and score a ``GridSearchCV`` over their parameters. This gets you up to ``expt_34`` in ``models.py``.
    - typically, my gridsearch process is two-step: first, get the right order of magnitude for the hyperparameters (centering on the default values is a reasonable place to start, since the library devs are very smart), followed by a narrower parameter range around the most successful values from the first round
- score a combination of those same top three models (now with their optimized hyperparameters) using [ensemble estimators](http://scikit-learn.org/stable/modules/ensemble.html) (bagging, boosting, and voting approaches). This also included some gridsearches to explore variants in the ensemble hyperparameters. This gets you up to ``expt_44`` in ``models.py``, including the winning model #42. 

Finally, having exhausted the ``scikit-learn`` API, I experimented with:

- using the leaderboard to reverse engineer the actual distribution of test labels, and assign model prediction weights accordingly (in the top-three models)
- [installing the development branch](http://scikit-learn.org/stable/developers/contributing.html#git-repo) of ``scikit-learn`` where there is a forthcoming "multilayer perceptron" neural network classifier, and gridsearching on that model.

Neither of these approaches improved upon my ensemble approach in #42. So, at this point, I turned to some data engineering.

After some literature research, it seemed that generating "new data" by means of transforming the original data was a common tactic (recall the mantra that "more data is better"). I found some code that shifted each of the images by one pixel (up, down, left, and right), and so I modified and reimplemented it for my own use (``expand-np-arrays.py``). The result is a 4x increase in the amount of training data (we now have a 250,000 x 784 matrix). This process takes a while (about 20 minutes) and results in a new, 2-GB ``numpy`` array to train a model on.

Since there were less than 24 hours until the competition deadline (and I figured it would take at least 5x as long to train), I chose not to explore any cross-validation. Instead, I [threw a hail mary](https://www.youtube.com/watch?v=iCemfI5L-y0) and went straight to training my best-yet model (#42) on the entire larger dataset to create a leaderboard submission. Training on this data took 16 hours (versus 1.5 with the original data), but did yield a leaderboard accuracy improvement of 0.5% (98.68%). This was my highest accuracy. 

<center>
<blockquote class="twitter-tweet" data-conversation="none" lang="en"><p lang="en" dir="ltr">much better. <a href="https://t.co/56Tn0tHtl9">pic.twitter.com/56Tn0tHtl9</a></p>&mdash; Josh Montague (@jrmontag) <a href="https://twitter.com/jrmontag/status/678674010519920641">December 20, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>

# Take-aways

This classification task was super fun! It was also really interesting to hear how the rest of my team approached the problem. There were a bunch of smart things they incorporated or tried that I didn't: 

- dimensionality reduction through PCA or SVD (clearly not all the pixels are necessary!) 
- calculating and classifying the images based on their [moments](https://en.wikipedia.org/wiki/Image_moment) (clever!) 
- manipulations with [``scikit-image``](http://scikit-image.org/docs/dev/auto_examples/) (an entire library for image manipulation!)
 
Those were all good ideas; I'll aim to keep them in mind for the next similar task. The other things I took away were: 

- designing for fast iterations is 👍 
- designing around robust logging is 👍 
- parametrization (decoupling) is 👍 
- simple shell/operating system "parallelization" is much easier than full-on distributed computing (if you don't already have that down, I suppose) [^legos] 
- I can definitely benefit from a deeper understanding of model selection 
- I can definitely benefit from a deeper understanding of feature and data engineering 
- since I very intentionally shared this code, next year's competition is going be tough

That's about it - feel free to poke around in [the actual code, too](https://github.com/jrmontag/mnist-sklearn)!



[^3dollars]: This is an approximation, but I think it's pretty close for spinning up a new Ubuntu EC2 instance, take 30 minutes to install all the system and Python bits (including the ``virtualenv`` creation), and then train the winning model (#42, ~1.5 hours). For another ~$30, you could earn an additional 0.5% accuracy by expanding the data (~20 minutes) and training the same model on the larger dataset (~16 hours). 

[^yan]: In the repo ``Makefile``, I go out and get the binary data from Yan LeCunn's website, the canonical leaderboard (and history lesson) for MNIST classification. In our competition, these files were just handed to us. 

[^legos]: This is how I typically think, but was also well-articulated recently in ["Lego Blocks for Big Data"](http://www.pixelmonkey.org/2015/11/30/legos).

