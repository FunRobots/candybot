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


api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)


class TwitterEvent():
	def checkMentionInTwitter(code):
		# print("\n Start checkMentionInTwitter, code = {}".format(code))

		#GetMentions is fast to detect mention of @fun_robots account (in few seconds)
		mention = api.GetMentions(count=5, since_id=None, max_id=None, trim_user=False, 
			contributor_details=True, include_entities=True)
		for status in mention:
			status_dict = json.loads(str(status))
			# print("\n PRINT mention: \n", status_dict.keys(), "\n")

			tw_text = status_dict.get('text')
			# print(tw_text, "\n")  ##for debug

			if code in tw_text:
				print("PLEASE, TAKE YOUR CANDY! :)))))))))")
				print(status_dict.get('user_mentions'), "\n")
				print(tw_text, "\n")
				return(True)

		return(False)


