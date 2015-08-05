---
layout: post
title: New beginnings, a recap, and reflection
---

It's hard to believe that it's been over a year since I last posted on MattVukas.com. Between issues with Wordpress hosting and life generally getting in the way, I haven't had time to write much. But a lot has happened since my last post in July 2014.

I started a new job. Did some stuff. BlaH. Here's a cool pic:

![Fiber optic picture that is super cool](/images/fiber-optics.jpg)

Here's some super cool code I wrote:
{% highlight ruby %}
def show
  @widget = Widget(params[:id])
  respond_to do |format|
    format.html # show.html.erb
    format.json { render json: @widget }
  end
end
{% endhighlight %}

Third paragraph here lol.