---
layout: post
title: Landing a FAANG Dev Job in 2020
coverImage: /images/faang-companies.png
---

Earlier this year, I started thinking about if it might be time for me to make a career change. I had been at my current company, a growth mode startup, for almost two and a half years, and the company had changed a lot during that time. My life had also changed a lot during that time. And any experienced developer (especially [here in Colorado](https://markets.businessinsider.com/news/stocks/top-12-tech-hubs-in-the-us-according-to-bloomberg-2019-11-1028700143)) gets _a lot_ of messages from recruiters about jobs on a regular basis. I was starting to consider the opportunities out there, and I came to the realization that I wanted to try for a software engineering position at a large, _mega cap_ tech company. You know, a **FAANG** (Facebook, Amazon, Apple, Netflix, Google) job.

<figure>
  <img src="/images/faang-companies.png" />
  <figcaption>
    The FAANG acronym was <a href="https://www.investopedia.com/terms/f/faang-stocks.asp">coined by CNBC host Jim Cramer</a> and is now somewhat synonymous with <a href="https://en.wikipedia.org/wiki/Big_Tech">"Big Tech"</a>. Some use the term FAANG+ to include other prominent tech companies like NVIDIA and Twitter.
  </figcaption>
</figure>

There's a lot out there already about generally what it's like to interview at these big tech companies, so I don't intend this to be a comprehensive guide. Rather, this is a guide to the general process of getting a FAANG dev job through the lens of my own experience, here in the Denver/Boulder area, with 6+ years of experience and a few dev jobs under my belt.

## Preparation

This is where I spent the most amount of time during this whole process, so let's start here. Big tech interviews are daunting, and some of the material is only tangentially related to your typical day-to-day work as an engineer, so it's worth allotting some time to study before the actual interview.

### Coding Interview Prep

I don't know about you, but I've never had to [invert a binary tree](https://twitter.com/mxcl/status/608682016205344768) during my work as a full stack web developer. Or reverse a linked list. Et cetera. The typical whiteboard interview feels more related to a CS data structures class you may have taken during college, than to the the daily job of a software engineer, and [many have poked fun at that](https://twitter.com/catalinmpit/status/1237992452230918144). We can debate endlessly the best way to interview software engineers, and there's certainly pros and cons to the current paradigm. But you can think of this as a sort of standardized test; an on-the-spot aptitude test. It's a test that you can maximize your chances for with a bit of preparation.

Big tech interviewing has turned into a cottage industry of its own. We have the classic ["Cracking the Coding Interview"](https://amzn.to/3cknJ7w), authored by an ex-Google employee, which was the gold standard a few years ago. But things have become more intense. More recently, we have 1000+ question banks like [Leetcode](https://leetcode.com/), software engineer YouTubers such as [TechLead](https://www.youtube.com/channel/UC4xKdmAXFh4ACyhpiQ_3qBw), and paid algorithms & data structures courses such as [AlgoExpert](https://www.algoexpert.io/product). **There's an entire industry of individuals and companies making money off of the technical interview prep process.** It can all be a bit overwhelming as to where to start.

For me personally, what worked was spending most of my prep time on [Leetcode](https://leetcode.com/) and trying to brush up on several main categories that interviewers generally like to ask about:

- Arrays (including 2D arrays, partitioning, sorting)
- Binary trees
- Hashmaps & caching
- Linked lists
- Memoization
- Graphs (DFS & BFS)

And if you have time, you might review lesser asked categories as well such as: Tries, Heaps, Bitwise math, etc. Remember, you can prepare, but it's impossible to be 100% prepared for what you might encounter given the wide breadth of topics.

You read about people who spend A LOT of time "Leetcoding", solving hundreds of problems, and otherwise dumping a lot of time into "grinding" through the problem bank. Of course spending more time will increase your odds, but in my opinion, **it's more effective to do a few problems in each of these data structure categories rather than blindly trying to do as many problems as possible**.

Make sure you actually understand these CS fundamentals, the "building blocks" of common data structures and algorithms, before you dive head first into Leetcoding. If you have a computer science degree like me, you probably took at least one comprehensive data structures class in undergrad, and you might just need a refresher. If you are from a self-taught or coding bootcamp background, you might need more work here. Either way, [YouTube is your friend](https://youtu.be/pcKY4hjDrxk), and you might look into more comprehensive learning such as [AlgoExpert](https://www.algoexpert.io/product).

<figure>
  <img src="/images/chalkboard-lecture.jpg" />
  <figcaption>
    Pictured: typically what the board looks like after you wrap up your 45 minute coding interview.
  </figcaption>
</figure>

### System Design Interview Prep

In addition to the _writing code on a whiteboard_ interview that you'll likely have several of during an on-site, for candidates above a certain seniority level, you'll also have a system design interview. This is a vague, open-ended question where the interviewer will ask you to sketch out how you'd implement the architecture of a large system. Interviewers might ask you to implement a well known service like Twitter or Uber. Also common is for interviews to ask you to design a system related to their line of work.

This part of the interview is worth preparing for, but in my opinion, deserves less time than the coding prep. If you're an experienced developer, you've likely architected systems of your own and thought through:

- Microservices and how different concerns should be broken up into different services
- Load balancing at a high level using tools like NGINX
- Databases and schema design, as well as SQL versus NoSQL
- Caching strategies, possibly using tools such as Redis
- Leveraging message queues and pub-sub technologies
- For larger services or codebases, leveraging object-oriented design principles

Just to name a few things. If you haven't had recent experience architecting systems (especially distributed systems), it's worth spending some time here. I like the [system-design-primer](https://github.com/donnemartin/system-design-primer) on GitHub as a starting point. I also like [Tushar Roy's videos on YouTube](https://youtu.be/UzLMhqg3_Wc) - he has a few where he talks about various system design concepts and then goes through some sample problems.

### Behavioral Interview Prep

The behavioral or "cultural" interview is essentially the non-technical part of the interview. If you've done at least a few interviews in your life (even outside of tech), you should be pretty familiar with this one. People commonly poke fun at the most common questions like "what's your biggest weakness?" and most people are at least somewhat familiar with what to expect here.

In my opinion, if you already feel pretty comfortable with interviewing in general, you don't have to spend much time here. It's good to spend at least a bit of time brainstorming good _interview fodder_ from your last 1 or 2 jobs (projects that went well, conflicts you handled, projects you'd do differently, etc), and thinking about how you might describe these situations with the [STAR method](https://www.themuse.com/advice/star-interview-method). Depending on the company you're interviewing for, you might think about picking situations from your past that align with their corporate values (ex: Google's ["Ten things we know to be true"](https://www.google.com/about/philosophy.html)).

<figure>
  <img src="/images/office-space-bobs.jpg" />
  <figcaption>
    Don't be surprised if you're interviewed by two or more people (like in this <a href="https://youtu.be/_iiOEQOtBlQ">classic scene from the movie Office Space</a>). Often, one of the interviewers is shadowing or training, and it's really no different from the standard 1-on-1 interview that most people are more comfortable with.
  </figcaption>
</figure>

## Interview Process

When it comes to actually interviewing, your first step will be applying to jobs and scheduling interviews. If you're lucky, you might already have relationships with recruiters via LinkedIn, Email, or other channels, who can definitely expedite this process for you. It also helps (but certainly isn't necessary) to get a referral from an employee currently at the company. From what I understand, this could help nudge you through the application/resume screen stage, and the person referring you usually gets a little bonus if you get hired.

FAANG+ interviews generally consist of 1) some kind of high-level call with a recruiter, 2) a technical phone screen that may last an hour or so, and 3) an on-site interview that takes 4-5 hours. When you get to the final stage, it's in your best interest to schedule a few of these on-sites in rapid succession, as that will make negotiation easier if you have multiple offers.

There's already a ton written on [Blind](https://www.teamblind.com/), [Leetcode](https://leetcode.com/), and other sources about what the different company on-site interviews may entail, so I won't discuss that here. But as a general piece of advice: make sure to talk through your thought process completely, ask clarifying questions, and in general _stay calm_. Whiteboard interviews are designed to be very difficult, it's normal to sweat a bit during them. If you get stuck, talking through your approach shows the interviewer generally how you might approach fuzzy or difficult problems, and interviewers might nudge you in the right direction or offer feedback if they're satisfied with how you're dissecting the problem.

## Parting Thoughts

If you've completed all the previous steps and get to the point where you have at least one job offer... congratulations! Now comes the easy part. If you have multiple offers, think about which company you'd actually prefer to work for. If their offer is lacking, feel empowered to go back and ask for more. Generally, everything is negotiable, but companies may be more willing to budge on one-time items (such as signing bonus) versus stock or equity. Also, feel free to ask for an extension on an offer deadline if you need more time to negotiate or decide. Companies are generally willing to extend these deadlines if you give a reason. As of 2020, I feel that [Levels.fyi](https://www.levels.fyi/) is the most up-to-date source for compiled compensation info, so check there first. [Blind](https://www.teamblind.com/) and [Leetcode](https://leetcode.com/) "Discuss" are also decent sources of unfiltered info (including total comp figures) about tech companies.

If you did not get an offer, don't despair! The bar at FAANG+ companies is very high, with the logic being that they would rather generate false negatives than false positives. At most of these companies, you can reapply after 6 months or so if you were turned down. And even with lots of studying, you can't guarantee yourself 100% odds in these interviews, so try not to let a negative hiring decision get you down.

If you read the [CS Career Questions subreddit](https://www.reddit.com/r/cscareerquestions/), [Blind](https://www.teamblind.com/), and other forums for tech workers, you'll find many people who landed a FAANG+ job and ultimately didn't find the satisfaction they were looking for. There are so many different types of companies that a dev can work at in 2020, the best fit for you might end up being a startup or totally different type of company. Good luck and happy job hunting!
