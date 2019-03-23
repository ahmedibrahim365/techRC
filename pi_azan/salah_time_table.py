#!/usr/bin/env python

import numpy as np
import pandas as pd

from datetime import date
import requests
import json
from pprint import pprint


# reading table contents from URL
contents = pd.read_html('http://theictn.org/prayertimetable.aspx')
pprint(contents)

if date == date.today():
    print(contents)
else:
    print('not today')


# IN TESTING...

# Creating Class with date/time values
#class contents:
#    def __init__(self, date):
#        self.contents = date.today
#        self.contents = pd.DataFrame()