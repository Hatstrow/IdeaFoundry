import os, twitterKeys
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

class StdOutListener(StreamListener):
	
	def on_data(self, data):
		print(data)
		return true

	def on_error(self, status):
		print(status)

if __name__== "__main__":

	ConsumerKey = "KHYLrEV6YgzaeuKluwpqnMVoE"#twitterKeys.CONSUMER_KEY
	ConsumerSecrect = "P1doLmv851kQM9pcvFGPQXdsp9l2leN3hk8QwPsmdiEOUOzDLQ" #twitterKeys.CONSUMER_SECRET
	AccessToken =  "953111613170683905"#twitterKeys.ACCESS_TOKEN
	AccessSecret = "BZOX55QQpfn2HHQ279c1x5vKPqvCHXLTOvot4E7RcsDRE"  #twitterKeys.ACCESS_TOKEN_SECRET

	print(ConsumerKey) 
	print(ConsumerSecrect) 
	print(AccessToken) 
	print(AccessSecret) 


	Listener = StdOutListener()
	auth = OAuthHandler(ConsumerKey,ConsumerSecrect)
	auth.set_access_token(AccessToken,AccessSecret)

	stream = Stream(auth,Listener)

	stream.filter(track = ['hello'])
