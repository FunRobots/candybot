#CandyBot
==========

##About
Candybot is a simple bot that gives a candy for social actions. Run from a Raspberry Pi.

Current version: v0.2

##Changelog:
v0.2 - Add Twitter Stream API to listen tweets, remove button (started twitter api request to check bot mentions in tweets). It works faster and overcome api time rate limit. 

v0.1 - First prototype. But listen whether his name is mentined in Twitter, 
	as well as a secret code he give to a User. If user tweet a message with 
	@fun_robots and some secret code, he will get a candy. Just simple, just fun




##Instructions for makers
______________________

1. Setup your RaspberryPi with python environment 
	
* ``sudo pip install twitter``  (download https://pypi.python.org/pypi/twitter with stream methods) 
* ``sudo apt-get install python3-gpiozero``
* ``sudo easy_install -U RPIO``

2. Setup config for Twitter 
	Workapble packages: python-twitter  (or twython, tweepy)

3. Clone git repository 

4. Create file secret.py and add the following strings (don't forget to put real credentials there):
	
	TW_CONSUMER_KEY='put_your_consumer_key_here'
	TW_CONSUMER_SECRET='put_your_consumer_secret_here'
	TW_ACCESS_TOKEN_KEY='put_your__access_token_key_here'
	TW_ACCESS_TOKEN_SECRET='put_your_access_token_secret_here'

5. Run ``sudo python candybot.py``

##References for examples and tips
_________________________________

### Using Twitter Stream API
* http://socialmedia-class.org/twittertutorial.html 

