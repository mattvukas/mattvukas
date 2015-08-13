# Copyright Matt Vukas 2015
import requests
from termcolor import colored

with open("OLD-SITEMAP.xml") as f:
  for line in f:
    url = line.rstrip('\r\n')[20:] # strip away http://mattvukas.com part
    r = requests.get('http://www.mattvukas.com' + url)

    codeColor = 'red'
    if r.status_code == 200:
      codeColor = 'green'
      if "<link rel=canonical href=\"http://www.mattvukas.com/\">" in r.content:
        codeColor = 'blue' # redirecting to root

    if url == '':
      url = '(root)'

    print colored(str(r.status_code), codeColor) + " | " + url