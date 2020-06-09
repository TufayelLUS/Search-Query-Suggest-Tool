#!/usr/bin/python3
# -*- coding: utf8 -*-
# Special thanks to bing for the suggestion API page :)
# Subject to change any time and this repository will not be maintained in the future!
# What is the use of this?
# This script allows you to search for a term and returns you a possible search suggestion based on the term given
# requires python3 to work
import requests
from urllib.parse import quote
import re
my_search = str(input("Enter your search query(ex. Ban): "))
my_search = quote(my_search)
resp = requests.get(
    f'https://www.bing.com/AS/Suggestions?pt=page.home&mkt=en-us&qry={my_search}&cp=1&cvid=598B65DD7BA942F1BB3BD7DBEC926785').text
queries_suggested = re.findall(r'query="([\w\-\'\_\@ ]+)"', resp)
# when searched Ban, returns ['bank of america', 'banana bread recipe', 'banana republic', 'bandcamp', 'bangladesh', 'bankrate', 'bandana face mask', 'bandlab']
print(queries_suggested)
# now run a loop in queries_suggested and work on your project ...
