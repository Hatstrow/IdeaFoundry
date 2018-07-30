import os#, twitterKeys
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import keys as k
import json

class Authenticater():
	def Auth(self):
		ConsumerKey = k.ConsumerKey
		ConsumerSecrect = k.ConsumerSecrect
		AccessToken = k.AccessToken
		AccessSecret = k.AccessSecret
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
		stream = Stream(auth,listener, tweet_mode= 'extended')

		stream.filter(track = hash_tag_list)

class StdOutListener(StreamListener):
	'''
	This is a basic listener class that just prints received tweets to stdout
	'''
	

	def on_data(self, data):
		try:
			streamed_tweets = json.loads(data)
			if streamed_tweets['text'][0:2] == 'RT':
				return True
			else:	
				if "extended_tweet" in streamed_tweets:
					text = streamed_tweets['extended_tweet']['full_text']
					print('this is extended' + '' + text)
				else:
					text = streamed_tweets['text']
					print('this is not extended' + '' + text)

				print(streamed_tweets)
			
			#for i in x.keys():
				#print(i)
			# print(text)
			# Tweeter = streamed_tweets['user']['screen_name']
			# theyareFrom = streamed_tweets['user']['location']
			# print(Tweeter + "" + theyareFrom)
			# time = streamed_tweets['timestamp_ms']
			# print(time)
			# if streamed_tweets['coordinates'] != 'null':
			# 	Location = streamed_tweets['coordinates']
			# print(Location)
			# popularity = streamed_tweets['retweet_count'] + streamed_tweets['favorite_count']
			# print(popularity)
			# # print(Tweeter + Location + time + popularity + "" + text)

			#with open(self.fetched_tweets_filename, 'a') as tf:
			#	tf.write(data)		0
			return True
		except BaseException as e:
			print("error on_data: %s" %str(e))
			return True
	
	def on_error(self, status):
		if status == 420:
			print('About to get booted')
			print(status)
			return False

		return True


if __name__== "__main__":
	hash_tag_list = ["dogs"]
	fetched_tweets_filename = "tweets.txt"

	twitter_streamer = twitterStreamer()
	while twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list):
		print("hello")
	



