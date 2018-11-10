# -*- coding: utf-8 -*-
import requests, json 
import csv
from collections import defaultdict

from geopy.geocoders import Nominatim
columns = defaultdict(list) 
with open('strava_tweets2.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k
geolocator = Nominatim(user_agent="my-application")
locations_coordinates = []
for lak in columns['location']:
    if lak:
        kal = unicode(lak, "utf8", errors="ignore")
        print kal
#     if kal:
        location = geolocator.geocode(kal.split()[0])
        print location.address
# # Fron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
        locations_coordinates.append((location.latitude, location.longitude))
    else:
        locations_coordinates.append(lak)
print locations_coordinates