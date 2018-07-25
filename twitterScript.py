import os#, twitterKeys
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

class Authenticater():
	def Auth(self):
		ConsumerKey = "KHYLrEV6YgzaeuKluwpqnMVoE"#twitterKeys.CONSUMER_KEY
		ConsumerSecrect = "P1doLmv851kQM9pcvFGPQXdsp9l2leN3hk8QwPsmdiEOUOzDLQ" #twitterKeys.CONSUMER_SECRET
		AccessToken =  "953111613170683905-pg8dFZHpXpLD5v8mqELcMUcOevPmwEq"#twitterKeys.ACCESS_TOKEN
		AccessSecret = "BZOX55QQpfn2HHQ279c1x5vKPqvCHXLTOvot4E7RcsDRE"  #twitterKeys.ACCESS_TOKEN_SECRET
		auth = OAuthHandler(ConsumerKey,ConsumerSecrect)
		auth.set_access_token(AccessToken,AccessSecret)
		return auth

class twitterStreamer():
	'''
	Class for streaming and processing live tweets
	'''
	def __init__(self):
		self.Authenticaterr = Authenticater()
	def stream_tweets(self, fetched_tweets_filename,hash_tag_list):
		listener = StdOutListener()
		auth = self.Authenticaterr.Auth()
		stream = Stream(auth,listener)

		stream.filter(track = hash_tag_list)

class StdOutListener(StreamListener):
	'''
	This is a basic listener class that just prints received tweets to stdout
	'''
	def on_data(self, data):
		try:
			print(data)
			#with open(self.fetched_tweets_filename, 'a') as tf:
			#	tf.write(data)		
			#return True
		except BaseException as e:
			#print("error on_data: %s" %str(e))
			return True
	def on_error(self, status):
		if status == 420:
			print(status)
			return False

		return True


if __name__== "__main__":
	hash_tag_list = ["hello"]
	fetched_tweets_filename = "tweets.txt"

	twitter_streamer = twitterStreamer()
	while twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list):
		print("hello")
	

