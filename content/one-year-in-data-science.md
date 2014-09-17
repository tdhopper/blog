Title: One Year In: Data Scientist
Slug: one-year-in-data-scientist
Date: 2014-09-03
Tags: career, business
Summary: A look back at some of the major changes in my transition from graduate student to data scientist. 

*Updated:* *after a particularly full week recently, another important topic came to mind that I felt would be valuable to include here: "keeping the wheels on the cart." You can find that section at the bottom.* 

This summer marked just over one year since I donned a goofy hat, shook my advisor's hand, promised my parents they'd never have to attend another graduation ceremony, and received the piece of paper that declared I was done with higher education.[^school] About the same time, I started working full-time as a data scientist at a small-ish software company. It seems like the one year mark is as good a time as any to pause and reflect, maybe for both my own sake and for that of anyone wondering, "Josh, what were the biggest changes you experienced in your first year that could be helpful for someone interested in making a similar transition?" Maybe no one is actually wondering that... but writing is healthy, so here you go anyway. 

I should start with some context; even though this kind of story will be different for everyone, I can at least give an idea about the "from" and "to". Before this transition, I spent six years in graduate school studying physics. As is common for these programs, there were two or three years of coursework followed by (and overlapping with) three or four years of research. When I left the lab, I started working full-time at a software ([SaaS](http://en.wikipedia.org/wiki/Software_as_a_service)) company of about 50 people.[^path] My role (and that of my small team) was best described as "internal consultancy": doing research and providing answers to technical questions that came from sales, marketing, product, and engineering. This required varying levels of software development and analysis in a handful of languages and environments: predominantly a shell command line (bash), Python, and R. 

Ok, on to the more interesting stuff; what were the biggest changes in this transition? 


## Time

The first change I noticed was the perception and use of time. In graduate school, the relevant time scales were something along these lines: 

- (**substantial research contribution** aka graduation: *five to six years*)
- **major result** journal article / funding proposal: *one year*
- **minor result** conference paper / presentation: *three months* 
- **fractional progress** incremental work toward minor results: *one week to one month*

Particularly in my experimental research, "fractional progress" was simply the nitty gritty bit of getting actual work done: "successfully collecting dataset X," or "completing the analysis of dataset Y," or "finally building the op-amp with the proper gain and signal-to-noise ratio." 

In contrast, I vividly recall the first urgent task I was assigned in my new role, which came with a followup of "we really need these answers soon - like tomorrow." Now, first and foremost: when made frequently, that kind of request can be a real red flag about the perceived value of your time. Thankfully, this was an exceptional case and most requests do not come with a priority-level-9 urgency. But that experience was an extreme example that frames the idea. Relevant time scales in the business world are shorter. I've found the scales to be more along these lines:

- **major result** delivery of all projects for quarterly goals: *three months* 
- **minor result** success / progress on individual projects: *one month*
- **fractional progress** incremental work toward minor results: *one day to one week* 

As an aside: you may not have thought about time in units of "quarters" before, but in a business setting, you will. See also, the **Business** section, below.

In this case, "fractional progress" / day-to-day work is pretty similar in scale, but covers many more potential areas: working through a particular data collection or analysis, bug fixes and new features in software and tools, customer conversations and support, putting together presentations for meetings or Meetups, and all manner of assorted other things. Any one of these may be a small (or large) part of a bigger project that provides business value.  

*Punchline: time is "shorter"; progress is measured more frequently.* 

## Drivers

A bigger change, still, was the shift in the motivation and drivers of the work. When I joined my research lab, there was already some research momentum from previous work. For my own research, I took a fork of that previous work and mostly tugged on the interesting threads to see where they led. Now, there were some implicit things at work there, too; for example, my advisor had enough experience to feel that my research was worthwhile and capable of being pitched to funding agencies. But, beyond that, the research directions were - as a favorite professor once described[^intuition] - very much a "follow your nose" experience. Use your intuition and best judgement, but let the path be guided by the new and unexpected discoveries that occur along the way.  

In my new role, my team is guided by a similar sense of exploration within any particular project (undoubtedly related to fact that we're mostly former research scientists). But the selection of what projects we work on is driven much more by the business needs. Will this project help the industry move forward? Will it drive interest in our products or help us better understand the current use of our services? Does it directly benefit a customer? Does it ultimately lead to revenue for the company? Even though our team is not a software development team, most of our colleagues are; so we try to work using some of the same principles. This means "should we work on X?" is often decided by how close the [user story](http://en.wikipedia.org/wiki/User_story) gets to the actual business customer. 

*Punchline: exploration and following intuition is required, but stay focused on things that will provide business value.* 

## Business

The <s>last</s> penultimate idea I'll mention is around what it means to be a "business." I'll admit that I previously had approximately zero understanding of what came along with - and was considered part of - a business. At some level, it had to mean that there is a product or service (maybe more than one), and revenue came in from somewhere. For example, consumers could pay the business for the product. Or, consumers can use the product for free while being shown advertisements, and those advertisers would contribute revenue to the business for the opportunity to display ads. Or maybe all of the funding comes from an actual person or another business (angel or venture investments) in the hope that someday they'll create a successful product that ends up in one of the first two categories (and subsequently provide a return on investment for whomever provided the initial funds). Anyway, this is all perspective that I have *now*, but I had no idea about this before. 

One of the most overwhelming changes I experienced was the range of different people and teams involved; it turns out it takes a lot of cooperative, functional teams to make a successful business. Wrapping my head around the acronyms: BD, PMs, AMs, ... I struggled for quite a while trying to understand and internalize the roles that all of these people had. Oh, and those ones are: business development, product (or project) manager (or sometimes "product marketing", just to mess with you), and account managers. Finding out the roles that each of these groups of people (and all the rest!) have within the company is really helpful for understanding your own place and value. Don't be shy about asking folks what they do; it helps identify ways you can be assests for one another. 

*Punchlines: 1) funding has to come from somewhere; it's helpful to understand what - and to whom - your business owes its existence. 2) It takes a lot of different roles to really make a business rock.[^headcount] It takes time to comprehend how everyone fills their niche, but learning the roles is crucial.* 

## "Keeping the wheels on the cart"

Finally, if you're lucky (and good at what you do), there will always be more people requesting your time and effort than you have to give. Being in demand is typically a good thing. What this means, however, is that it's up to you to learn where to draw the lines around what you can successfully deliver. Additionally, even when you think you've drawn your lines reasonably and conservatively, unexpected things will arise. Curveballs are sneaky and inevitable. The server is down, the VPN isn't working, the file is 10x bigger than you thought it would be, there's some previously-unheard-of error for which the holy trinity (Google, StackOverflow, and IRC) are powerless. It happens; the key is not freaking out. 

When the path gets rough and the produce (your projects) starts to fall out of the cart, the key is to focus on keeping the wheels on the cart. Keep your focus on preventing the wholesale collapse of the vehicle (and the subsequent disappointment of all involved stakeholders), and then sort out your issues. This may mean compromising on some of the results, so it's helpful to understand the minimum acceptable version. Ideally, your typical approach is to knock projects out of the park, so it's unlikely that anyone will notice the difference between that and these rare times when you've compromised. 

Transparency goes a long way, too. So, it may even be worth describing how your result differed from what you were hoping to achieve. Your mileage may vary.  

*Punchline: Learn your limits. Focus on keeping things moving when you approach those limits.* 
 

## Now What?

So, what's the takeaway? Unfortunately, I can't help you figure out your new data-related role in a business outside of the research lab (but, hey, congrats on finding something!). But, I hope these thoughts shine a bit of light on some of the challenges I ran into related to the approach and awareness that I brought from my previous role in academic research. Everyone's circumstances are a little different, so you may not experience any of these; or maybe you have more. Either way, good luck in your new path!


[^school]: Barring, of course, any unexpected impulses to set off for an MBA or MD.

[^path]: Having writen this, it feels like there's also an opportunity for a companion article about the particular path that led me to now; I've added it to my list; stay tuned. 

[^intuition]: Part of the reason this line was so memorable was that it came while our mid-career professor was trying to explain how we should use our intuition to solve path integrals in quantum mechanics.  

[^headcount]: Again, this is from the perspective of a company with ~50 people. At an earlier stage, there were five or six people, so everyone had to do their best to wear multiple hats.






