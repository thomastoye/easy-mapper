#!/usr/bin/env python

import json
import csv
#from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
import time

children = []

with open('data') as csvfile:
  reader = csv.reader(csvfile, delimiter=';', quotechar='"')
  for row in reader:
      children.append({ 'childId': row[0], 'firstName': row[1], 'lastName': row[2], 'address': row[3] })

print(children)

geolocator = GoogleV3()

for child in children:
    location = geolocator.geocode(child['address'])
    if location:
      child['geolocation'] = location.raw
    with open('output', 'w') as outfile:
        json.dump(children, outfile, sort_keys = True, indent = 2)
    time.sleep(3)

