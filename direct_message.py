from twython import Twython, TwythonError
import tweepy
# -*- coding: utf-8 -*-
# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from random import randint
from time import sleep
import time

CONSUMER_KEY = '34F4k92NA2Xe4MC3Q7HtKnpqj'
CONSUMER_SECRET = '0apeln9QxMPSkpy7MnGOuOZexCAw9K6uhNQemAxjGvLuZtT85k'

ACCESS_TOKEN = '3305953796-FdenybpO5lD8ctLwqDTzjieNPbN6R8bBrzXNBA3'
ACCESS_TOKEN_SECRET = 'JcI3GwtIRUMklmu215MnTCsmAux1KmiOQBS4hdsxfs4WM'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,
				  ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

def substract(a, b):                              
    return "".join(a.rsplit(b))
# api = tweepy.API(auth)
# event = {
#   "event": {
#     "type": "message_create",
#     "message_create": {
#       "target": {
#         "recipient_id": '4905756225'
#       },
#       "message_data": {
#         "text": 'This is a test'
#       }
#     }
#   }
# }
# # api.send_direct_message_new(event)

# # api.send_direct_message(event)
# api.send_direct_message_new(event)
# photo = open('PSOSM_message to users-1.png', 'rb')
# response = twitter.upload_media(media=photo)
# twitter.update_status(status='Checkout this cool image!', media_ids=[response['media_id']])

#text = 'Hi <first name>,\nGreetings! We recently observed that you are a very active user on Strava, though your various tweets about your activities.. We are a research group based out of IIIT Hyderabad, conducting a research on the Privacy and Security concerns with the user-location based information given out by Strava.\nYou may be aware that Strava has a privacy setting called Privacy Zone, where a user can choose to hide an area of a particular radius in her/his maps, usually which could reveal possibly sensitive locational details about her/him. Even with this privacy feature in place, there is evidence that users could still be vulnerable to a privacy attack. \nOpting out of posting your activity is not always a solution as there are times when you want to acheive that rank in the leaderboard of a particular segment or flaunt about your recent hike.\nWe are not an anti-Strava group, but a group of pro-Strava academicians who want to find out the existing problems with privacy on Strava and hence report it to them, for the benefits of all users like you!\nBut we need your help for that! We have created an Official Application through the Strava API. If as a Strava user, you agree to authenticate our app and allow us access to your data, which you have made public, we can work on making Strava a better companion of ours. We assure you that since this is an Official Strava App, through this authentication, WE ONLY receive you information that you have made public on Strava and no other sensitive information. \nTo authenticate, please click on the link below and select the "Authorize" button on the page.\n bit.ly/StavaPrivacyResearch\nWho are We?\nWe are a team of researchers in IIIT Hyderabad, India, with our professor-guide being Dr.Ponnurangam Kumaraguru(PK). We are a legitimate group of researchers and you can check us out on twitter, Facebook!\nThanks for your support'
# new_text = 'Who are We?\nHi, my name is Shravya, MS student at IIIT Hyderabad. You can check me out on twitter, Facebook and LinkedIn! My team-mates are Devansh and Arhant.\nTo authenticate, please click on the link below and select the "Authorize" button on the page.\nbit.ly/StavaPrivacyResearch'
# username = 'devanshmanu'
maxlen = 0
minlen = 1000
tweet = '\nbit.ly/StavaPrivacyResearch.'
k = len(tweet)
count = 0
photo = open('PSOSM_message to users-1.png', 'rb')
response = twitter.upload_media(media=photo)
l = open('user_list.txt').readlines()
for n in range(len(l)):
# 	if len(username)>maxlen:
# 		maxlen = len(username)
# 	if len(username)<minlen:
# 		minlen = len(username)
	tweet += '@'+ l[n].strip('\n')+' '
	# print tweet
	if len(tweet)>=280:
	# 	# tweet.split('@')[]
	# 	print tweet
	# 	if len(tweet)>280:
	# 		substract(tweet,'@'+ username.strip('\n')+' ')
	# 		print len(tweet)
	# 		print tweet
	# 	# tweet -= '@'+ username.strip('\n')+' '
		# twitter.update_status(status=tweet, media_ids=[response['media_id']])
		# print "tweeted"
		# wait = randint(100,150)
		# print 'wait: '+str(wait)+' seconds'
		# time.sleep(wait)
		# print tweet
		# print len(substract(tweet, '@'+ l[n].strip('\n')+' '))
		print substract(tweet, '@'+ l[n].strip('\n'))
		tweet = '\nbit.ly/StavaPrivacyResearch.'
		tweet += '@'+ l[n].strip('\n')+' '
		count +=1

print tweet
# twitter.update_status(status=tweet, media_ids=[response['media_id']])
# print "tweeted"
# print count + 1
# print minlen, maxlen
	# # print username
	# # # try:
	# # tweet = 'Hi @'+username+', support our project. You can check us here:\nhttps://www.linkedin.com/in/shravya-kanchi/, https://in.linkedin.com/in/devanshmanu.\nTo authenticate, please click on the link below and select the "Authorize" button on the page.\nbit.ly/StavaPrivacyResearch'
	# photo = open('PSOSM_message to users-1.png', 'rb')
	# response = twitter.upload_media(media=photo)
	

	# # # except:
	# # 	print "not tweeted"
	# 	pass