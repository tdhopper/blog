Title: Vignette: Create a Text File of U.S. State Names
Slug: state-names
Date: 2014-06-09
Tags: vignette, bash, shell, munge 
Summary: Create a simple text file of U.S. state names with minimal typing. 

While working on a project recently, I needed a simple list of US State names. My goal was to have a plain text file, one state per line, no funny business. The order of the states wasn't important. I always like a command-line challenge, so my first thought was "find the list online somewhere, `wget` or `curl` as needed, slice up the html, and be done."[1]

So, I went to [the source of all information](http://en.wikipedia.org/wiki/Main_Page), and lo! there is a [table](http://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States#States) whose first column is all the US states. *#fistpump* The only problem is I really wasn't planning to parse HTML for this little exercise; seems like a bit of overkill. But then I noted the `[edit]` link next to the table name...

![Wikipedia table edit button](/images/state-table.jpg "Yes, this will definitely work.")

... and clicked through that to observe just the table source. Now this we can work with! 

I simply copy/pasted this plain text into a file locally (say, `states-table.txt`). Then, had a look:


    $ head -n30 states-table.txt 
    ==States==
    {| class="wikitable sortable plainrowheaders" style="text-align: right;"
    |+ States of the United States
    !scope="col" width=12%|State
    !scope="col" width=1%|[[List of U.S. state abbreviations|Abbr.]]
    !scope="col" width=8%|[[Capital city|Capital]]
    !scope="col" width=12%|Largest city{{#tag:ref|The largest city is the city in a state with the largest population in the [[city proper]]; [[metropolitan area]]s are not considered in this number.|group=upper-alpha|name=a}}<ref name="State and Local Government Finances and Employment">{{cite web|url=http://www.census.gov/compendia/statab/2012/tables/12s0448.pdf|title=State and Local Government Finances and Employment|year=2012|publisher=[[United States Census Bureau]]|pages=284|type=pdf|accessdate=July 8, 2013}}</ref>
    !scope="col" width=11% data-sort-type="date"|Statehood
    !scope="col" width="12%"|Population<br>(2013 est)<ref name=PopEstUS>{{cite web|url=http://www.census.gov/popest/data/state/totals/2013/tables/NST-EST2013-01.xls|title=Table 1. Annual Estimates of the Population for the United States, Regions, States, and Puerto Rico: April 1, 2010 to July 1, 2013|format=[[Microsoft Excel]]|work=2013 Population Estimates|publisher=[[United States Census Bureau]], Population Division|date=December 2013|accessdate=January 12, 2014}}</ref>
    !scope="col" width=12%|Total area in mi<sup>2</sup> (km<sup>2</sup>){{#tag:ref|Area figures are rounded to the nearest whole number.|group=upper-alpha|name=b}}<ref name="2010 Census of Population and Housing">{{cite web|url=http://www.census.gov/prod/cen2010/cph-2-1.pdf|title=2010 Census of Population and Housing|date=September 2012|publisher=[[United States Census Bureau]]|pages=41|type=pdf|accessdate=July 8, 2013}}</ref>
    !scope="col" width=12%|Land area in mi<sup>2</sup> (km<sup>2</sup>)<ref group=upper-alpha name=b /><ref name="2010 Census of Population and Housing" />
    !scope="col" width=12%|Water area in mi<sup>2</sup> (km<sup>2</sup>)<ref group=upper-alpha name=b /><ref name="2010 Census of Population and Housing" />
    !scope="col" width=1%|[[List of United States congressional districts|House seat(s)]]
    |-
    !scope="row"|{{flag|Alabama}}
    |AL
    |[[Montgomery, Alabama|Montgomery]]
    |[[Birmingham, Alabama|Birmingham]]
    |December 14, 1819
    |4,833,722
    |{{Convert|52420|mi2|km2|sigfig=6|abbr=values|sortable=on}}
    |{{Convert|50645|mi2|km2|sigfig=6|abbr=values|sortable=on}}
    |{{Convert|1775|mi2|km2|sigfig=4|abbr=values|sortable=on}}
    |7
    |-
    !scope="row"|{{flag|Alaska}}
    |AK
    |[[Juneau, Alaska|Juneau]]
    |[[Anchorage, Alaska|Anchorage]]
    |January 3, 1959 


Clearly there's a lot of extra formatting for the other columns, but we can see a couple of the state names, so we can definitely observe some patterns. A simple `grep` and `sed` combination get us almost to the finish line:

    $ cat states-table.txt | grep "flag|" | sed 's/^.*flag|//;s/}}.*//'
    Alabama
    Alaska
    Arizona
    Arkansas
    California
    Colorado
    Connecticut
    Delaware
    Florida
    Georgia (U.S. state)|name=Georgia
    Hawaii
    ...

One extra bit of `sed` formatting (strip anything that's not a letter)... 

    $ cat states-table.txt | grep "flag|" | sed 's/^.*flag|//;s/}}.*//;s/ [^a-Z].*$//'
    Alabama
    Alaska
    Arizona
    Arkansas
    California
    Colorado
    Connecticut
    Delaware
    Florida
    Georgia
    Hawaii

... and we're good to go! (note: if you're doing this on OS X, you may have to swap that last `sed` range for `[^a-zA-Z]`) 
 
It's always nice to flex your command-line fu.



[1] In hindsight, I clearly could have spent an extra 30 seconds on google and just copypasta'd the results from a site like [this one](http://liststates.com/). But where's the fun in that?? 

