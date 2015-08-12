---
layout: post
status: publish
published: true
title: Learn the one weird CSS trick that THEY don't want you to know about!
author:
  display_name: mvukas
  login: mvukas
  email: mattvukas@gmail.com
  url: ''
author_login: mvukas
author_email: mattvukas@gmail.com
wordpress_id: 356
wordpress_url: http://mattvukas.com/?p=356
date: '2014-01-17 00:46:17 -0700'
date_gmt: '2014-01-17 05:46:17 -0700'
---
**Web Developers HATE him! Code maintainers CAN'T STAND him!**

In all seriousness though, I've just stumbled across a great CSS hack that I couldn't help but share. I was working on a Wordpress site for a client, and I had almost gotten everything lined up perfectly, when suddenly I ran into a snag. For whatever reason, a div was getting a strange padding value hardcoded onto it somewhere along the line, using inline CSS. Now in my mind, inline CSS is the end all be all of CSS, so there was no way to get around this strange issue without delving into some custom Javascript or finding the core issue in the theme or Wordpress itself. There's nothing that can override inline CSS code, right?

Well that, ladies and gentlemen, happens to not be true. It was news to me, at least. Apparently, the problem of rogue inline CSS code is easily remedied. For example, let's say you have this code causing a problem:

{% highlight html %}
<div id="blah" style="padding-top: 60.5px; padding-bottom: 60.5px;">
  Lorem ipsum dolor sit amet, consectetur adipiscing elit
</div>
{% endhighlight %}

Just jump into your CSS style sheet, and add this rule:

{% highlight css %}
#blah[style] {
  padding-top: 15px !important;
  padding-bottom: 15px !important;
}
{% endhighlight %}

The [style] tag means that it overrides whatever is specified as the "style" value within the HTML tag. The !important tag essentially inputs the nuclear launch codes into CSS - it's an order that should not be taken lightly, and carries grave consequences for future code maintainers. It gives that particular rule top priority, outside the usual CSS chain of command. But in this case, if there's no other way to get rid of that pesky inline style rule, it's warranted. Use sparingly.

*Credit goes to <a href="http://css-tricks.com/override-inline-styles-with-css/">css-tricks.com</a> for informing me about this great little hack*
