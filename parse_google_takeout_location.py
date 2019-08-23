import json
import os
import sys
import geojson 
from geojson import Feature, Point, FeatureCollection, dump
from datetime import datetime
from datetime import date
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file',
	help='file to read')
parser.add_argument('-p', '--pipe', action='store_true',
	help='pipe data')
parser.add_argument('-s', '--save', action='store_true',
	help='just save geojson')
# parser.add_argument('-x', '--xyz', action='store_true',
# 	help='upload file to an XYZ space')


sourcefile = 'Location History.json'

results = parser.parse_args()
print(results)
sourcefile = results.file
if results.file == '':
    sourcefile = results.file
    print('reading from' + sourcefile)

features = []

class Object(object):
    pass

props = Object()
sys.stdout.write('parsing ')

with open(sourcefile) as json_file:
    data = json.load(json_file)
    count = 0
    for p in data['locations']:
        lat = p['latitudeE7']/10000000
        lon = p['longitudeE7']/10000000
        point = Point((lon,lat))
#         accuracy = {"accuracy": p['accuracy']}
#         accuracy = {"accuracy": p['accuracy']}
        accuracy =  p['accuracy']
        timestamp = int(p['timestampMs'])/1000
        date = date.fromtimestamp(timestamp)
#         print(date.weekday())
        date_time = int(datetime.utcfromtimestamp(timestamp).strftime('%Y%m%d%H%M%S'))
        hour_min = int(datetime.utcfromtimestamp(timestamp).strftime('%H%M'))
        year = int(datetime.utcfromtimestamp(timestamp).strftime('%Y'))
        year_month = int(datetime.utcfromtimestamp(timestamp).strftime('%Y%m'))
        month = int(datetime.utcfromtimestamp(timestamp).strftime('%m'))
        year_month_day = int(datetime.utcfromtimestamp(timestamp).strftime('%Y%m%d'))
        hour = int(datetime.utcfromtimestamp(timestamp).strftime('%H'))
        day_of_week = date.weekday()
        
        if 'velocity' in p.keys():
            velocity = p['velocity']
        else:
            velocity = ''
            
        if 'heading' in p.keys():
            heading = p['heading']
        else: 
            heading = ''
            
        if 'altitude' in p.keys():
            altitude = p['altitude']
        else:
            altitude = ''
            
        
        tags = ["year@"+str(year),"year_month@"+str(year_month),"month@"+str(month),"day_of_week@"+str(day_of_week),"hour@"+str(hour)]
#         t = ','.join(tags)
#         print(tags)

        props = {
            "accuracy": accuracy,
            "hour_min": hour_min,
            "date_time": date_time,
            "year": year,
            "year_month": year_month, 
            "month": month,
            "year_month_day": year_month_day,
            "hour": hour,
            "day_of_week": day_of_week,
            "velocity": velocity,
            "heading": heading,
            "altitude": altitude,
            "@ns:com:here:xyz": 
                {
                    "tags": tags
                }
            }
#         print(props) # good for troubleshooting

# 
#         props.accuracy = accuracy
#         props.timestamp = timestamp
#         props.time = time
#         props.year = year
#         props.year_month = year_month
#         props.year_month_day = year_month_day
#         props.hour = hour
#         props.day_of_week = day_of_week
#         print(props.year)
#         json_props = json.dumps(props)
        features.append(Feature(geometry=point,properties=props))
        count = count + 1
        
        if count%100 == 0:
        	sys.stdout.write(str(count))
        	sys.stdout.write('... ')

feature_collection = FeatureCollection(features)
print(count)

if not results.pipe: # save the file unless we try to pipe it
	filename = "google_takeout_location_history.geojson"
	with open(filename, 'w') as f:
		print('saving ' + filename)
		dump(feature_collection, f)

if not results.save and not results.pipe: # kick off an XYZ session on the CLI if we are only saving, or not piping 
	xyz = "here xyz upload -f %s -s"%(filename)
	print(xyz)
	os.system(xyz)
	print()

if results.pipe: # assuming you're doing stdout fun, like `this_script.py | here xyz upload`
	json.dump(feature_collection, sys.stdout, indent=4)
	print() # adds an extra newline
