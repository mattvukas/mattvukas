# MattVukas.com Github Pages repo

Source code for generating a static blog.

Example [link](http://daringfireball.net/projects/markdown/syntax#link) here.

Testing images:
![Fiber optic picture that is super cool](/images/fiber-optics.jpg)

Testing code highlighting:
{% highlight ruby %}
def show
  @widget = Widget(params[:id])
  respond_to do |format|
    format.html # show.html.erb
    format.json { render json: @widget }
  end
end
{% endhighlight %}

Final paragraph here. 