---
layout: post
title: Using GitHub Pages with a Naked Domain
coverImage: /images/mattvukas-com-dig-result.jpg
---

I've been tweaking a few things about this website, so I thought I'd share my learnings with everyone. This blog is powered by the static site generator [Jekyll](https://jekyllrb.com/), and it's completely static. You basically write your posts in Markdown, Jekyll generates a static site from those files, and then the static site can be served up very cheaply & easily from S3/CDN/blob storage of any sort. No server-side logic here. [GitHub Pages](https://pages.github.com/) makes it very simple to host this sort of website for free - you can see the repo for this website [here](https://github.com/mattvukas/mattvukas.github.io). I came across a bit of conflicting information about how to setup a custom "naked" domain (no `www`), so I'm sharing my setup here.

## Configuring Your DNS

Assuming you have enabled GitHub Pages for your static site repo, you'll next want to configure things over at your DNS provider (which may be the same as your registrar - I use [Namecheap](https://www.namecheap.com/)). You'll want to setup `A` records under your root domain pointing to these IP addresses:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

You might double check that these IP addresses are current at the [official docs here](https://help.github.com/en/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain). You'll also need to add a `CNAME` record pointing from `www` to your root domain. On your DNS provider dashboard, it should look something like this when complete:

![](/images/github-pages-dns.jpg)
_My DNS setup over at Namecheap_

## Sanity Check with `dig`

Using the command line tool `dig`, I would check `www.yourdomain.com` and verify that the DNS records look correct. Keep in mind that it may take 24-48 hours for DNS changes to propagate. Here's what my site's result looks like:

![](/images/mattvukas-com-dig-result.jpg)
_`dig` result for www.mattvukas.com_

## Configuring GitHub Pages

Now head back over to GitHub, go to Settings -> GitHub Pages for your site repo. You'll want to make sure your naked domain is saved under the "Custom domain" field. And you'll also want to check the "Enforce HTTPS" box. It may take some time for this to become available as your DNS update propagates:

![](/images/github-pages-settings.jpg)
_Setting things up in the GitHub Pages config section_

## The Final Result

To test things out, I would visit `www.yourdomain.com` and `yourdomain.com` in a web browser. If everything is setup correctly, they should both take you to the HTTPS naked domain `https://yourdomain.com`.

I would recommend GitHub Pages for anyone looking for a simple, performant, NoOps setup for a personal blog, or really any website hosting relatively static content. WordPress is overkill for most sites, and has had [so many security vulnerabilities](https://www.cvedetails.com/vulnerability-list/vendor_id-2337/product_id-4096/Wordpress-Wordpress.html) over the years...

GitHub handles the setup around HTTPS, puts a CDN in front of all their Pages, and will host your site for free if you're willing to put it up in a public repo. The [Google PageSpeed](https://developers.google.com/speed/pagespeed/insights/) results speak for themselves:

![](/images/mattvukas-com-pagespeed.jpg)
_Can't do any better than a perfect 100_

GitHub Pages provides fairly generous [usage limits](https://help.github.com/en/github/working-with-github-pages/about-github-pages#guidelines-for-using-github-pages), and it sounds like they'll kindly notify you before pulling the plug if you come close to hitting them. I'm not too worried about exceeding 100 GB of bandwidth a month, so I'll likely leave my site here for the long haul. 📈
