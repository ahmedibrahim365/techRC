#!/usr/bin/env python

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

from datetime import datetime
import requests
import json
from pprint import pprint


# Pandas
# navigating table contents from URL
url_mosque = ('http://theictn.org/prayertimetable.aspx')
url_mosque_icn = requests.get('https://www.muslimpro.com/en/Prayer-times-Nashville-TN-United-States-4644585')
contents = (url_mosque_icn, 'html.parser')

a = BeautifulSoup(url_mosque_icn.content, 'html.parser')
#

# Date filter
weekday_filter = datetime.now()
print(weekday_filter.strftime('%A'))
#


# using soup to extract single tag
url_type_find_all = a.find( class_="mp-widget-timetable").get_text()



print(url_type_find_all)
#print(url_pr_str, url_pr_str1)


