import os, twitterKeys
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

Class StdOutListener(StreamListenear):
	
	def on data(self, data):
		print(data)
		return true

	def on error(self, status)
		print(status)

if name__== "__main__":

ConsumerKey = twitterKeys.CONSUMERkEY
ConsumerSecrect =  twitterKeys.CONSUMERsECRECT
AccessToken =  twitterKeys.ACCESStOKEN
AccessSecret =  twitterKeys.ACCESStOKEN

Listenear = StdOutListener()
auth = OAuthHandler()
auth.set access token()
