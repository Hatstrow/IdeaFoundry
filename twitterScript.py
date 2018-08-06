import os#, twitterKeys
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import keys as k
import json
import pandas as pd
import numpy as np



class TheFilter():
	'''
	Class for importing filter file of all filters
	'''
	def file(self, fileName):
		FilterList = []
		try:	
			OriginalFile = open(fileName, 'r')
			for i in OriginalFile:
				FilterList.append(i.rstrip())
			OriginalFile.close()
			return FilterList
		except BaseException as e:
			print( 'error:  %s' %str(e))

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
		self.Authentification = Authenticater()
	def stream_tweets(self, fetched_tweets_filename,hash_tag_list):
		listener = StdOutListener()
		auth = self.Authentification.Auth()
		stream = Stream(auth,listener, tweet_mode= 'extended')
		print(hash_tag_list)
		stream.filter(track = hash_tag_list)

class dataGetter():
	'''
	Gets text regaurdless if its a RT or not 
	and if its either extended or not
	'''
	def OnlyTheText(self, data):
		try:
			streamed_tweets = data
			
			# stoperinit= TheFilter() #if i want to filter out specific phrases
			# stoper =stoperinit.file('theBad.txt')
			# for i in stoper:
			# 	if i in text:
			# 		return True

				
			#if "extended_tweet" in streamed_tweets : #gets full tweet either way 
				#text = streamed_tweets['extended_tweet']['full_text']
				#if not a RT but extended
				#print('etended   ' + text.strip())	
			if "extended_tweet" in streamed_tweets['retweeted_status']:
				print(data)
				#if its a RT and extended 
				text = streamed_tweets['retweeted_status']['extended_tweet']['full_text']	
				print('RT extended    ' + text.strip())
			#else:
				#can either be a RT or not, but is not longer for extended
				#text = streamed_tweets['text']
				#print('not extended   '+ text.strip())
			
			return text


		except BaseException as e:#throws error if from this class
			print('error in \'text only\' : %e' %str(e))


	#def Popularity(self,data):
		#if 

class StdOutListener(StreamListener):
	'''
	This is a basic listener class that just prints received tweets to stdout
	'''
	

	def on_data(self, data):
		try:
			streamed_tweets = json.loads(data)
			'''
			the above is for anything thats not text
			i'll probably add all that to the data getter class when I'm 
			ready too
			'''
			
		# 	stoperinit= TheFilter()
		# 	stoper =stoperinit.file('theBad.txt')
		# 	for i in stoper:
		# 		if i in text:
		# 			return True

				
		# 	if "extended_tweet" in streamed_tweets : #gets full tweet either way 
		# 		text = streamed_tweets['extended_tweet']['full_text'].rstrip()
		# 		#if not a RT but extended
		# 		print('etended   ' + text)	
		# 	elif "extended_tweet" in streamed_tweets['retweeted_status']:
		# 		#if its a RT and extended 
		# 		text = streamed_tweets['retweeted_status']['extended_tweet']['full_text'].rstrip()	
		# 		print('RT extended    ' + text)
		# 	else:
		# 		#can either be a RT or not, but is not longer for extended
		# 		text = streamed_tweets['text'].rstrip()
		# 		print('not extended   '+ text)

			theGetter = dataGetter()#inicciate dataGetter class
			streamed_tweetsFromClass = theGetter.OnlyTheText(streamed_tweets)
			
			
			#Tweeter = streamed_tweets['user']['screen_name']
			#theyareFrom = streamed_tweets['user']['location']
			#timeStamp = streamed_tweets['created_at']
			# if streamed_tweets['coordinates'] != None:
			# 	Location = streamed_tweets['coordinates']
			# else:
			# 	Location = 'No coordinates'
			#popularity = streamed_tweets['retweet_count'] + streamed_tweets['favorite_count']
			

			#with open('tweetData.txt', 'a+', encoding='utf-8') as tf:
				#tf.write(str(text) + "  END1 " + str(Location) + "  END2 " + str(popularity) + "   END3 " + str(Tweeter) + "  END4" + str(theyareFrom) + " END5 " + str(timeStamp) +"\n")
			

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
	IdeaFilter = TheFilter()
	IdeaFilterList = IdeaFilter.file('testFilter.txt')
	fetched_tweets_filename = "tweets.txt"
	print(IdeaFilterList)
	twitter_streamer = twitterStreamer()
	twitter_streamer.stream_tweets(fetched_tweets_filename, IdeaFilterList )
