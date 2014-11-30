__author__ = 'hkapadia'
#Get Tweets from twitter and parse them
import codecs
import sys
import tweepy
import util
from config import *
from term_lists import *
from util import safe_print


class GetTweets:

    #Do handling of secret key's in config file
    auth = tweepy.OAuthHandler(key, secret)
    api = tweepy.API(auth)
    parsedtweetdic = {}
    unparsedtweetdic = {}

    #TODO:Improve Parsing function. Parse on hashtags, violentterms, locality
    def parsetweet(self, tweet):
            #hashtags = tweet.hashtags.text
            tweetlower = tweet.text.lower()
            words = tweetlower.split()
            if any(x in violenttermslist for x in words):
                return True

    def printtweet(self, tweetlist):
        for tweet in tweetlist:
            print tweet.user.id, tweet.user.screen_name, safe_print(tweet.text), tweet.retweeted, tweet.retweet_count,  \
                    tweet.user.location, tweet.created_at

    #TODO:Exapand searchterm to include multiple terms and hastags. Capture geo location.
    def getparsedtweetsforsearctterm(self, searchterm, count, since_id):
        tweetlist=[]
        self.tweets = self.api.search(q=searchterm, count=count, since_id = since_id)
        for tweet in self.tweets:
            if self.parsetweet(tweet) is True:
                tweetlist.append(tweet)
        return tweetlist


    def getunparsedtweetsforsearctterm(self, searchterm, count, since_id):
        tweetlist=[]
        self.tweets = self.api.search(q=searchterm, count=count, since_id=since_id)
        for tweet in self.tweets:
            tweetlist.append(tweet)
        return tweetlist


