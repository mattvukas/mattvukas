# MattVukas.com GitHub Pages repo

Repository containing static site personal blog for one Matt Vukas.

GitHub repo: https://github.com/mattvukas/mattvukas.github.io

Generated website: http://www.mattvukas.com/

## Blog development

1. Make sure `ruby` is good to go
2. Make sure `bundler` is good to go
3. Make sure gems are setup correctly in `.bash_profile` or wherever
4. Run `bundler install`
5. Run `jekyll serve`

### Setting up dev on Windows bash shell

1. Install [VS Code](https://code.visualstudio.com/) and [Linux for Windows](https://docs.microsoft.com/en-us/windows/wsl/install-win10) (wow, what a time to be alive). Type `code .` in a bash prompt to [run VS Code in WSL](https://code.visualstudio.com/docs/remote/wsl). Pop that integrated terminal open in VS Code for convenience.
2. Set things up according to the [Jekyll docs here](https://jekyllrb.com/docs/installation/windows/#installation-via-bash-on-windows-10)
3. Run `bundler install`
4. Run `jekyll serve`

## Create a new post

`jekyll post "Title of the post"`

...
