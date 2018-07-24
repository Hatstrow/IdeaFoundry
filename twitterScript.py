import os#, twitterKeys
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
class twitterStreamer():
	'''
	Class for streaming and processing live tweets
	'''
	def stream_tweets(self, fetched_tweets_filename,hash_tag_list):
		Listener = StdOutListener()
		ConsumerKey = "KHYLrEV6YgzaeuKluwpqnMVoE"#twitterKeys.CONSUMER_KEY
		ConsumerSecrect = "P1doLmv851kQM9pcvFGPQXdsp9l2leN3hk8QwPsmdiEOUOzDLQ" #twitterKeys.CONSUMER_SECRET
		AccessToken =  "953111613170683905-pg8dFZHpXpLD5v8mqELcMUcOevPmwEq"#twitterKeys.ACCESS_TOKEN
		AccessSecret = "BZOX55QQpfn2HHQ279c1x5vKPqvCHXLTOvot4E7RcsDRE"  #twitterKeys.ACCESS_TOKEN_SECRET
		auth = OAuthHandler(ConsumerKey,ConsumerSecrect)
		auth.set_access_token(AccessToken,AccessSecret)

		stream = Stream(auth,Listener)

		stream.filter(track = hash_tag_list)

class StdOutListener(StreamListener):
	'''
	This is a basic listener class that just prints received tweets to stdout
	'''
	def on_data(self, data):
		try:
			print(data)
			with open(self.fetched_tweets_filename, 'a') as tf:
				tf.write(data)		
			return True
		except BaseException as e:
			print("error on_data: %s" %str(e))
			return True
	def on_error(self, status):
		print(status)

if __name__== "__main__":
	hash_tag_list = [""]
	fetched_tweets_filename = "tweets.txt"

	twitter_streamer = twitter_streamer()
	twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)





	ConsumerKey = "KHYLrEV6YgzaeuKluwpqnMVoE"#twitterKeys.CONSUMER_KEY
	ConsumerSecrect = "P1doLmv851kQM9pcvFGPQXdsp9l2leN3hk8QwPsmdiEOUOzDLQ" #twitterKeys.CONSUMER_SECRET
	AccessToken =  "953111613170683905-pg8dFZHpXpLD5v8mqELcMUcOevPmwEq"#twitterKeys.ACCESS_TOKEN
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
