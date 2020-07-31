#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from urllib.parse import quote

headers = {
    'device-memory': '8',
    'dnt': '1',
    'dpr': '1',
    'ect': '4g',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'service-worker-navigation-preload': 'true',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'viewport-width': '1366',
}
keyword = input("Enter keyword: ") #enter your location keyword to search
keyword = quote(keyword)
resp = requests.get('https://www.airbnb.com/api/v2/autocompletes?country=BD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&language=en&locale=en&num_results=5&user_input={}&api_version=1.1.1&satori_config_token=EhIiJQIiEhUAEhUAEjISEjISAA&vertical_refinement=homes&region=-1&options=should_filter_by_vertical_refinement%7Chide_nav_results%7Cshould_show_stays%7Csimple_search'.format(keyword.lower()),headers=headers).json()
results = resp.get('autocomplete_terms')
for result in results: # keyword based suggestions
    print(result.get('display_name'))
    #print(result.get('location').get('location_name'))
