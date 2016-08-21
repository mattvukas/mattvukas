---
layout: post
title: My SEO Tools Cheat Sheet
---
**For those looking for a TL;DR: [here's the list]({% post_url 2016-08-21-my-seo-tools-cheat-sheet %}#seoToolsList)** <br> In my [last post]({% post_url 2016-08-10-revisiting-old-software-projects %}), I talked about my plan to revisit an old side project of mine and begin development anew. The project is a Chrome extension called [Simple Blocker](http://simpleblocker.com/) that I started back in 2013. My first order of business was to fix a minor but long outstanding bug a few users had complained about, and my second order of business was to revamp the website for the app. The goal here being [SEO](https://en.wikipedia.org/wiki/Search_engine_optimization) and to improve my position on Google searches, and ultimately to drive new installs.

[Simple Blocker](http://simpleblocker.com/), being a desktop browser extension, is ultimately *a desktop application in a mobile world*, an app that will have to fight for survival in the era of shrinking desktop computer market share. When I designed the first iteration of the landing page, it was a static, non-responsive design that was really only usable on desktop browsers. This made sense, since my target audience was entirely made up of desktop users. But that assumption is now holding me back. **Even for a marketplace that consists entirely of desktop apps, the Chrome Web Store is optimized for mobile user conversions:**

![](/images/mobile-extension-discovery.jpg)
*Tried to look up my app on Safari for iOS. Instantly suggests the Chrome Web Store page, a desktop app store. Go there and it offers to send me a reminder when I get back to my desktop computer.*

Not to mention that Google will levy a [significant ranking penalty](https://www.sensiblemarketing.com/blog/google-penalty-for-non-mobile-sites) if your site doesn't fit their mobile-friendly criteria. After a bit of research, it was clear that my app would benefit from a revamped, [responsive](https://en.wikipedia.org/wiki/Responsive_web_design), mobile-first, [SoLoMo](https://www.youtube.com/watch?v=J-GVd_HLlps) website. 

And of course, I would subject my new landing page to a barrage of SEO tools and utilities to make sure my hard work pays off. Some of these tools I've known about for years, others I've discovered at work or more recently while building the new [Simple Blocker](http://simpleblocker.com/) site. All of them I would consider essential when designing a website with search engine presence in mind.

## <a name="seoToolsList"></a>The List

### Building Your Website

#### [Google Structured Data Testing Tool](https://search.google.com/structured-data/testing-tool)

This one can be useful depending on the type of website you're developing. Instantly test either isolated snippets of code or an entire website to make sure you're set up correctly for Google [rich cars and rich snippets](https://developers.google.com/search/docs/guides/mark-up-content). Having the correct meta markup can be a make-or-break detail for SEO, especially if you're relying on Google's news article snippets or Google Maps location snippets to drive a large part of your traffic. 

#### [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)

If you anticipate social discovery being an important traffic driver for your website (it usually is), Facebook's meta debugger is worth checking out. It checks the usage of [OG tags](http://ogp.me/) on your website and also gives you a preview of the rich snippet Facebook users will see when a link is shared on their app.

#### [Responsinator](https://www.responsinator.com/)

This is a simple app that lets you enter the URL for your site, then renders it across various screen sizes (desktop, tablet, mobile) on a single page. A very useful way to do a sanity check when developing a responsive site that should be accessible across a wide variety of devices.

#### [Retina-friendly Images Guide](http://ivomynttinen.com/blog/a-guide-for-creating-a-better-retina-web)

A very well written guide for both understanding and implementing best practices for 2x/Retina images. Fuzzy, scaled-up images are not what you want your users to see when accessing your site on hi-res mobile screens or Retina MacBooks.

#### [Favicon Cheat Sheet](https://github.com/audreyr/favicon-cheat-sheet)

Favicons are becoming increasingly important for user experience, with many different formats required across a variety of devices. In addition to being a long time staple of desktop favorites lists, hi-res favicons can be displayed prominently on the home screens of mobile devices. This comprehensive guide lets you make sure you're supporting the wide variety of formats. I'd also recommend this site which does a lot of the heavy lifting for you: [Real Favicon Generator](http://realfavicongenerator.net/)

### Testing and Optimizing Your Website

#### [Google Pagespeed Insights](https://developers.google.com/speed/pagespeed/insights/)

A very important tool for both SEO and user experience. This utility doesn't actually measure your page load speed, but instead scores your site based on several metrics and tests that directly correlate to fast page loading and rendering. Pagespeed Insights weights mobile performance heavily, and some of the tests are hard to pass, such as "Eliminate render-blocking JavaScript and CSS in above-the-fold content". But the goal here shouldn't be to score 100, only to improve your site's score and fare well against competitor websites. Keep in mind that even some Google websites [score poorly](/images/google-news-pagespeed.png) against the strict standards of this SEO checker.

#### [Pingdom Website Speed Test](https://tools.pingdom.com/)

Whereas the Pagespeed Insights tool just checks a variety of website attributes that correlate to better speeds, this tool actually runs a live network test against your site from one of several origin servers. You'll get an actual page load time, a performance rating, and detailed metrics about all of the file requests needed to render your page. This one also offers some advice about areas to improve on. I would recommend testing with both Pagespeed Insights and the Pingdom Speed Test for any site.

#### [CloudFlare](https://www.cloudflare.com/)

CloudFlare is a bit controversial in how much of your hosting infrastructure it replaces, as well as how it behaves as a reverse proxy, standing between your web host and the rest of the Internet. But CloudFlare is trusted by millions of websites, and I'll also vouch for it. It provides a variety of SEO-boosting services to you with no effort and (usually) no cost. Upgrading to HTTPS, minifying assets, boosting speed with a CDN, mitigating DDoS attacks, managing cache control - these are just a few of the benefits CloudFlare can bring to your site. 

#### [SEO Site Checkup](http://seositecheckup.com/)

This polished SEO checker is a handy way to check many different SEO best practices at once. There are some limits on use, such as the number of sites/reports you can run on the free plan, but a subscription may be worth it depending on your use case.

### Monitoring Your Website

#### [Google Analytics](https://analytics.google.com/)

Most people already know about Google Analytics, but it is an absolutely essential tool for evaluating SEO efforts. Not only can you see how much traffic you're getting, but you can also check out traffic sources and Google searches or social media referrals that are driving traffic.

#### [Google Webmaster Tools](https://www.google.com/webmasters/tools/)

Another well known tool, Google provides these utilities which let you ensure your site plays well with their web crawlers. You can check your search result appearance, debug structured data, submit your site to their index, and be notified of crawl errors.
