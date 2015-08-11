---
layout: post
title: New beginnings, a recap, and reflection
---
It's hard to believe that it's been over a year since the last time I posted something to [MattVukas.com](http://mattvukas.com/). I'm still alive, don't worry. I guess life has just gotten in the way of publishing anything longer than a tweet or collection of pictures on Facebook. Web hosting issues have caused some headaches as well, but that is sorted out now. Since my [last post on 7/8/2014](http://mattvukas.com/2014/07/08/medium-tumblr-re-consolidation-online-publishing/), a lot has happened in my life:

1. Launched [nowTweets](http://nowtweets.com/), a social web app I created
2. Left Bloomington, IN and moved to Kansas City
3. Started working at Cerner as a Software Engineer
4. Launched [Exaday](http://exaday.com/), a tech news website I created
5. Got engaged
6. Quit working at Cerner
7. Left Kansas City and moved to [Denver](https://www.youtube.com/watch?v=mqkxQQygzXg)
8. Started working at [Placeable](http://www.placeable.com/) as a Software Engineer
9. Migrated my blog from self-hosted Wordpress to [Jekyll](http://jekyllrb.com/) on [GitHub Pages](https://pages.github.com/)

I think that pretty much sums it up. Since this is mainly a tech blog, let's focus on the most recent tech-related story there. 

## Why did I leave Wordpress behind?

**Wordpress is really bloated.** It churns even on a decent server, between the massive pile of legacy PHP code that makes up Wordpress itself and the plugins that most admins (myself included) give free rein to. Pretty soon, you're installing caching plugins to try and deal with the poor performance caused by everything else. At that point, the performance issues you have would make even the Windows Vista developers blush.

**Hosting websites is hard.** With a self-hosted Wordpress instance, you need a server that can handle a sizable LAMP stack and occasionally handle heavy traffic. Hosting costs money. Even if you get a sweetheart deal like I did and host Wordpress for free on a dedicated server, you still have to deal with proper caching, setting up a CDN, and managing the endless stream of Wordpress vulnerabilities and related updates. It was just all overkill for a simple blog.

##But why is Jekyll on GitHub Pages so awesome?

**It's all based on Git and GitHub.** This makes things sooo easy. Just create a new file, write the post in Markdown, then commit and push it to `master`. I can even write post-commit hooks to automagically tweet my new articles or send out newsletters. Plus, the fact that my blog is just a GitHub repo means that the data (and change log) is backed up and secure. 

**Nothing beats free, managed hosting.** That's essentially what GitHub Pages is. A self-hosted Jekyll website would already be a huge improvement, since it's static and essentially immune to DDOS or *The Reddit Effect*. But being hosted on GitHub Pages means that there will almost never be a hosting issue, there is no "glue" to setup between my local work and the public-facing website, and there's no bill to pay at the end of the month.

**Everything is simple, open-source, and there's no vendor lock-in.** To be fair to Wordpress, it is open source, and you can pull all your content from a self-hosted instance in the form of HTML/CSS/PHP and exported SQL stuff. But this new setup has my blog as an open source repo with all my posts as HTML or Markdown files. It doesn't get much simpler than that. I like the fact that I'm not relying on 20 plugins from X number of devs to keep basic blog functionality running, and that I more or less understand every line of code powering this new blog.

## Going forward

With a nice, new, clean website design (work in progress) on a solid blogging platform, I'll probably be writing articles a lot more often. I've had a lot of interesting experiences since I moved to Denver in early June, and I've run into some new challenges doing Java webdev at Placeable, among other things. I think my blogging career may have peaked with the infamous ['Comcast is throttling Netflix' article](http://mattvukas.com/2014/02/10/comcast-definitely-throttling-netflix-infuriating/) of February 2014, but I plan to keep making attempts at quality content, because I do enjoy writing. I'm not sure if I'll write something that scandalous again, but maybe I'll get lucky with one or two good insights about programming. So keep your eyes peeled for new stuff soon.
