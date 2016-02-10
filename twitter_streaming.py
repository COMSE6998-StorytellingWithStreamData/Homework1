#!/usr/local/bin/python

#credits to http://adilmoujahid.com/posts/2014/07/twitter-analytics/

#This code receives tweets from Twitter. Then it filters the tweets content by New York
#and NBA. After that, it finds the user IDs who may be interested in New York and NBA,
#and print the user IDs on stdout.

#Please note this code doesn't contain user credentials to access Twitter API. Please
#apply user credentials by using your own Twitter account and fill it in before running
#this file.

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from sys import stdout

#Variables that contains the user credentials to access Twitter API 
access_token = "Put your access token here"
access_token_secret = "Put your access token secret here"
consumer_key = 	"Put your consumer key here"
consumer_secret = "Put your consumer secret here"


#This is a listener prints the user IDs who may be interested in New York and NBA on stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
    	#We only want to print the user ID, so we need to find the start point of the user ID.
        start = "id"
        #We only want to print the user ID, so we need to find the end point of the user ID.
        end = "id_str" 
        #Find user ID by giving start and end point of the user ID
        id_NY_NBA = data[data.find(start) : data.find(end)]
        #print user IDs who may be interested in New York and NBA on stdout.
        print id_NY_NBA
        #force clean the cache, since WebSocket only update the output when refresh the cache.
    	stdout.flush()
    	return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'New York', 'NBA'
    stream.filter(track=['New York', 'NBA']) 
    

    