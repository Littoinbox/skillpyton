# -*- coding: utf-8 -*-
from datetime import date, datetime
from pprint import pprint

import requests
import json

with open('city.list.json') as ff:
    sites = json.load(ff)

# aa = {'id': 707860, 'name': 'Hurzuf', 'country': 'UA', 'coord': {'lon': 34.283333, 'lat': 44.549999}}

count = 0
start, till = datetime(year=2018, month=1, day=1), datetime(year=2018, month=12, day=31)
start, till = int(start.timestamp()), int(till.timestamp())
for site in sites:
    if site['country'] == 'RU':
        print(site['name'])
        url = (f'http://history.openweathermap.org/data/2.5/history/city?'
               f'id={site["id"]}'
               f'&type=hour'
               f'&start={start}&end={till}'
               f'&appid=b1b15e88fa797225412429c1c50c122a1')
        print(url)
        response = requests.get(url)
        pprint(response.json())
        count += 1
        break
print(count)

# for k, v in sites.iteritems():
#     print(k, v)


# response = requests.get('http://samples.openweathermap.org/data/2.5/history/city?id=2885679&type=hour&appid=b1b15e88fa797225412429c1c50c122a1')
# print(response.json())
