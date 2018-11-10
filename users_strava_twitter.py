from twython import Twython, TwythonError
import json
import csv
import requests
from bs4 import BeautifulSoup
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

CONSUMER_KEY = 'KHTmO4MQe7hduK3T8C77gYxhL'
CONSUMER_SECRET = 'lPMxqGmFsoMPcbUfIslRYiMY5aaoq0j32etYcJgu13Se1PrlF3'

ACCESS_TOKEN = '931546201802940417-24ckatrdLwfv5wnjN6MFWzYJytJ3fMx'
ACCESS_TOKEN_SECRET = 'q2UeZLra1MTtaYQbq8ri6DOLMa79sqhpHluDJ2xEzSzou'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,
				  ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

def strava_url(url):
	if 'athletes' in url:
		return url
	else:
		try:
			page = requests.get(url)
			soup = BeautifulSoup(page.content, 'html.parser')
			# print soup.prettify()

			mydivs = soup.findAll("a", {"class": "avatar-content"})
			for tag in mydivs:
				if tag['href']:
					return 'https://www.strava.com'+ tag['href']
		except:
			pass


tweets = []
# MAX_ATTEMPTS = 1000
# COUNT_OF_TWEETS_TO_BE_FETCHED = 4000 

# for i in range(0,MAX_ATTEMPTS):

#     if(COUNT_OF_TWEETS_TO_BE_FETCHED < len(tweets)):
#         break # we got 500 tweets... !!

#     #----------------------------------------------------------------#
#     # STEP 1: Query Twitter
#     # STEP 2: Save the returned tweets
#     # STEP 3: Get the next max_id
#     #----------------------------------------------------------------#

#     # STEP 1: Query Twitter
#     if(0 == i):
#         # Query twitter for data. 
#         results = twitter.search(q="strava",count='100')
#     else:
#         # After the first call we should have max_id from result of previous call. Pass it in query.
#         results = twitter.search(q="strava",include_entities='true',max_id=next_max_id, count=100)

#     # STEP 2: Save the returned tweets
#     for result in results['statuses']:
#         # tweet_text = result['text']
#         tweets.append(result)


#     # STEP 3: Get the next max_id
#     try:
#         # Parse the data returned to get max_id to be passed in consequent call.
#         next_results_url_params = results['search_metadata']['next_results']
#         next_max_id = next_results_url_params.split('max_id=')[1].split('&')[0]
#     except:
#         # No more next pages
#         break
count = 0

results = twitter.cursor(twitter.search, q='strava', count=5000)
for result in results:
	if result not in tweets:
		tweets.append(result)
		# print result
		count += 1

results = twitter.cursor(twitter.search, q='#strava', count=5000)
for result in results:
	if result not in tweets:
		tweets.append(result)
		# print result
		count += 1

results = twitter.cursor(twitter.search, q='Strava', count=5000)
for result in results:
	if result not in tweets:
		tweets.append(result)
		# print result
		count += 1

print result
# print type(result)
# count = len(list(set(tweets)))
# k = sum(1 for x in results)
# print len(k)
print count
# print len(tweets)
flag = 0
outweets = []
with open('strava_tweets2.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerow(["url", "id", "user","text", "coordinates", "place", "source", 'location']	)
	for post in tweets:
		if post['entities']['urls']:
			with open('tweet_urls.txt', 'a') as the_file:
				# print post['entities']['urls'][0]['expanded_url']
				k = strava_url(post['entities']['urls'][0]['expanded_url'])
				if k:
					if type(post['id_str'])=='unicode':
						l = post['id_str'].encode('utf-8', 'ignore').decode('ascii')
					else:
						l = post['id_str']
					if type(post['user']['screen_name'])=='unicode':
						m = post['user']['screen_name'].encode('utf-8', 'ignore').decode('ascii')
					else:
						m = post['user']['screen_name']
					if type(post['text'])=='unicode':
						n = post['text'].encode('utf-8', 'ignore').decode('ascii')
					else:
						n = post['text']
					if type(post['place'])=='unicode':
						o= post['place'].encode('utf-8', 'ignore').decode('ascii')
					else:
						o= post['place']
					if type(post['user']['location'])=='unicode':
						p = post['user']['location'].encode('utf-8', 'ignore').decode('ascii')
					else:
						p = post['user']['location']
					if type(post['coordinates'])=='unicode':
						r = post['coordinates'].encode('utf-8', 'ignore').decode('ascii')
					else:
						r = post['coordinates']
					if type(post['source'])=='unicode':
						s = post['source'].encode('utf-8', 'ignore').decode('ascii')
					else:
						s = post['source']
					writer.writerow([k, l, m, n, r, o, s, p])
