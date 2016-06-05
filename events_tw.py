#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter
import json
# from twython import Twython
from secret import (
	TW_CONSUMER_KEY,
	TW_CONSUMER_SECRET,
	TW_ACCESS_TOKEN_KEY,
	TW_ACCESS_TOKEN_SECRET
)

consumer_key=TW_CONSUMER_KEY
consumer_secret=TW_CONSUMER_SECRET
access_token=TW_ACCESS_TOKEN_KEY
access_token_secret=TW_ACCESS_TOKEN_SECRET


api = twitter.Api(consumer_key=TW_CONSUMER_KEY,
	consumer_secret=TW_CONSUMER_SECRET,
	access_token_key=TW_ACCESS_TOKEN_KEY,
	access_token_secret=TW_ACCESS_TOKEN_SECRET)

# print(api.VerifyCredentials())


# search = api.GetSearch(term='#funrobots', include_entities=True)
# for line in search:
# 	print("\n PRINT search: \n", line)

class TwitterEvent():
	def checkMentionInTwitter(code):
		# print("\n Start checkMentionInTwitter, code = {}".format(code))

		#GetMentions is fast to detect mention of @fun_robots account (in few seconds)
		mention = api.GetMentions(count=5, since_id=None, max_id=None, trim_user=False, 
			contributor_details=True, include_entities=True)
		for status in mention:
			status_dict = json.loads(str(status))
			# print("\n PRINT mention: \n", status_dict.keys(), "\n")
			# for d in status_dict.keys():
				# print("\n PRINT key ", d, ": \n", status_dict.get(d), "\n")
				# print("\n PRINT key ", d, ": \n", status_dict.get('user_mentions'), "\n")

			# if status_dict.get('user_mentions'):
				# print(status_dict.get('user_mentions'), "\n")

			tw_text = status_dict.get('text')
			# print(tw_text, "\n")  ##for debug
			
			# if tw_text.find(str="#002", beg=0, end=len(tw_text)):

			if code in tw_text:
				print("PLEASE, TAKE YOUR CANDY! :)))))))))")
				print(status_dict.get('user_mentions'), "\n")
				print(tw_text, "\n")
				return(True)

		return(False)



