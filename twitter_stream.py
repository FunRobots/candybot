#!/usr/bin/python 

# Import the necessary package to process data in JSON format
try:
	import json
except ImportError:
	import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# from twython import Twython
from secret import (
	TW_CONSUMER_KEY,
	TW_CONSUMER_SECRET,
	TW_ACCESS_TOKEN_KEY,
	TW_ACCESS_TOKEN_SECRET
)

CONSUMER_KEY=TW_CONSUMER_KEY
CONSUMER_SECRET=TW_CONSUMER_SECRET
ACCESS_TOKEN=TW_ACCESS_TOKEN_KEY
ACCESS_SECRET=TW_ACCESS_TOKEN_SECRET


oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)


# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)



def listenTwitter(track, code):
	""" 
	Listen Twitter for mention of keywords stated in 'track' and 'code'. 
	Use Twitter stream API

    Params:
        track: message to track in Tweets 
        code: unique code from CandyBot
    Returns: 
        True or False decision status on candy dispensing 
    """

	# Listen for tweets with required track (@fun_robots) and #code  
	iterator = twitter_stream.statuses.filter(track=track)
	while True: 
		for tweet in iterator:
			tw_text = json.loads(json.dumps(tweet)).get('text')
			# print(tw_text, "\n")  ##for debug

			if code in tw_text:
				print("PLEASE, TAKE YOUR CANDY! :)))))))))")
				return(True)    
			else:
				break 
	return(False)


if __name__ == "__main__":
	get_candy = listenTwitter(track='@fun_robots', code='4451')
	print(get_candy)