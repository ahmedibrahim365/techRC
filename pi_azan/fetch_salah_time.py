#!/usr/local/bin/env python

from datetime import date
import requests
import json
from pprint import pprint


# Getting the website requests      /test by print
url_mosque = requests.get( 'http://theictn.org/prayertimetable.aspx' )
print( url_mosque )

# decoding the website to utf-8 format      /test decode by print
url_decode = url_mosque._content.decode('utf-8')
# pprint is hashed due to the length of the html. it will be filtered first
#pprint(url_decode)


print('---------------------------------------------------------------------A')      #separator
# using .headers to zoom in on site html data
url_headers = url_mosque.headers
print(url_headers)
print('---------------------------------------------------------------------B')      #separator
# determining hmtl context and default unicode
url_headers_content = url_mosque.headers['Content-Type']
print(url_headers_content)
print('---------------------------------------------------------------------C')      #separator
# Confirming(some of) the table values exist in URL
url_table_keyvalue = {'Date':'value1', 'Prayer Day':'Value2', 'Hijriy Day':'value3'}
url_parameters = requests.get('http://theictn.org/prayertimetable.aspx', params=url_table_keyvalue)
print(url_parameters)
print('---------------------------------------------------------------------D')      #separator





# IN TESTING...

# creating a function to group all prayers
def prayer_time():
    for prayer_table in url_mosque:
        fajr_start = 'Fajr Start'
        zhur_start = 'Zuhr Start'
        asr_start = 'Asr Start'
        maghrib_start = 'Maghrib Start'
        isha_start = 'Isha Start'
        if date > 24:
            return False
    return(fajr_start, zhur_start, asr_start, maghrib_start, isha_start)
print('---------------------------------------------------------------------E')      #separator




# using decoding to pprint html data in a readable view
#x = url_mosque.content
#pprint(x.decode('utf-8'))
#print('---------------------------------------------------------------------E')      #separator


# converting site to List


#url_site_content = get(url_local).json()['Prayer Timetable']

#pprint(url_site_content)

print('''Prayer Day
#Hijriy Day
#Fajr Start
#Fajr Jamaat
#Sun Rise
#Zuhr Start
#Zhur Jamaat
#Asr Start
#Asr Jamaat
#Maghrib Start
#Maghrib Jamaat
#Isha Start
#Isha Jamaat
#payload = {'key1': 'value1', 'key2': 'value2'}
#>>> r = requests.get('https://httpbin.org/get', params=payload)
#print(r.url)
#''')

