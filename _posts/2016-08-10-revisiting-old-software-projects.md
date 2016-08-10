---
layout: post
title: Revisiting old software projects
excerpt_separator: <!--more-->
---
Returning to long abandoned software project months or years after your last commit can be a daunting task. I should know - in my short career developing software I've left countless projects hanging. Some were left after the first commit, once I realized the idea just wasn't going to pan out. Others were fortunate enough to be left in a "mature" state after a flurry of work, yet lack documentation. In my current job at [Placeable](http://www.placeable.com/) I've been fortunate enough to work with a team that understands the importance of continuous integration, build automation, and easy deployments to production. These are lessons I had not yet learned when I worked on [Simple Blocker](http://simpleblocker.com/), which has no tests, no builds, no automation, and whose deployments involves me manually minifying, zipping, and uploading an archive to Google...

![](/images/raiders-idol.jpg)
*Seen here: trying to add a feature to a 2 year old codebase without breaking something.*

Taking another look at a legacy codebase can certainly feel like heading into ancient ruins of some sort. There is a vague memory of this place, but the key pitfalls or secrets have long been forgotten. It can be tricky and intimidating. It's hard for me to believe, but when I sat down to write this post I realized it had been almost an entire year since my last blog post. I guess I've been busy. I tried to remember how to write a new Jekyll post, which I hadn't documented in my readme of course, so I Googled it. Once that was done, I ran `jekyll serve` to try and spin up the site locally, and was met with cryptic Ruby dependency errors. I almost quit after that rough start, but I persevered and here we are. 

<!--more-->

## The payoff

Taking up old projects again can be rewarding. Or maybe the project was rewarding at one point and just needs some more attention. When I sat down to write a new blog article, I checked Google Analytics and saw that this site actually gets some traffic. Writing not only helps me organize my thoughts, but can help other people and sometimes even spark interesting discussions. My original [Comcast article]({% post_url 2014-02-10-comcast-definitely-throttling-netflix-infuriating %}) definitely sparked something and sort of made the whole blog experiment worthwhile to me.

## The first app I shipped

[Simple Blocker](http://simpleblocker.com/) holds a special place in my heart as the first *real* software project that I undertook and completed on my own. When I started on it in early 2013, I had just finished C211 Intro to Computer Science at [IU](https://www.indiana.edu/) and was beginning to take some more advanced CS classes in the spring semester. But I had a real hunger to continue teaching myself programming in my free time and develop an actual "app" which was becoming an incredible buzzword at the time. I had also grown a bit disillusioned with the overly academic nature of the CS program at IU, which taught many sources in [Scheme](https://en.wikipedia.org/wiki/Scheme_(programming_language)), whereas I wanted to learn languages that were actually used in industry that I could develop an app with. After testing the waters of mobile development, I did a few tutorials on JavaScript and enjoyed coding in it more than anything else I had used up to that point. I had been an avid user of browser extensions for Firefox and Chrome up to that point, and once I noticed how simple (and cheap) it was to publish Chrome extensions compared to my original dream of developing an iOS app, I was sold.

## Surveying the state of the project

Now at one point, [Simple Blocker](http://simpleblocker.com/) development took up a lot of my free time and I was improving it on a regular basis, as well as responding to user feedback. But once I ran out of ideas and deemed it "good enough", I moved on to other things and development paused.

![](/images/simple-blocker-repo.png)
*Dust has settled upon a once active git repo.*

It's been almost 2 years since I've made a commit. And my last commit was some minor maintenance stuff, so feature development has actually been stalled for over 2 years. But luckily for me, the app has worked well enough to be useful in all that time, and has gone from a few thousand users to 61,312 users as of today. I'm simply thrilled that so many people use my app, and the positive feedback I've received is great. But I've also received many complaints, feature requests, and emails from users.

![](/images/simple-blocker-requests.png)
*The real cost of software is in maintenance, they say.*

It's going to take some effort just to sort through all the feedback and decide on one or two actionable items here moving forward. There's a lot of overlap in the requests, and there's no doubt that something like a reverse-timer or a blocking schedule would be awesome. 

Sorting through that legacy code circa 2013 and making sure I don't break anything on apps that have been installed on people's computers for years - that will be a challenge. But improving the experience for my users, or getting to 100k installs, maybe getting some nice feedback - I think that makes it worth it. Either way, I'll document the experience here. [Simple Blocker](http://simpleblocker.com/) 1.0.0 here we come.
