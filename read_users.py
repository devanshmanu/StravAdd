import csv
from collections import defaultdict
import requests

columns = defaultdict(list) # each value in each column is appended to a list

with open('strava_tweets2.csv') as f:
	reader = csv.DictReader(f) # read rows into a dictionary format
	for row in reader: # read a row as {column1: value1, column2: value2,...}
		for (k,v) in row.items(): # go over each column name and value 
			columns[k].append(v) # append the value into the appropriate list
								 # based on column name k
k=  columns['user']
print len(k)
k = list(set(k))
print len(k)

valid_users = []

for username in k:
	try:
		request = requests.get('http://www.twitter.com/'+ str(username))
		if request.status_code == 200:
			# print('Web site exists')
			valid_users.append(username)
	except:
		pass
print len(valid_users)	
with open('user_list.txt','a') as j:
	for l in valid_users:
		j.write(l+'\n')