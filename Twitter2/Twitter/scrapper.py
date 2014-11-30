__author__ = 'hkapadia'
#The main program. Run this after creating DB and populating admin data
from get_tweets import GetTweets
from util import safe_print
from dbhandler import populatedb, getlatesttweetid, populateneighborhood, getalltweets
from term_lists import hashtags, Karachineighborhoodlist, subscribers,subscriberneighbohoods
from notification import sendmessage
import datetime


#Compares tweets from the previous day and marks it as a retweet if the text is exactly the same
def comparetweets(tweet, day):
    recordedtweetlist = getalltweets(day)
    for recordedtweet in recordedtweetlist:
        if recordedtweet.tweettext == tweet.text:
            return True
        else:
            return False

#Check if the tweet is a retweet as tweepy's retweet functionality is questionable.
def checkforretweet(tweet):
    if tweet.text.startswith('RT') == True:
        return 1
    elif comparetweets(tweet, 1) == True:
        return 1
    else:
        return 0

#Get the latest tweet id and call the search function
def sendnotifications(tweet,retweetcount,userfollowers):
    words=[]
    tweetlower = tweet.lower()
    words = tweetlower.split()
    if any(x in subscriberneighbohoods for x in words) and userfollowers>5 and retweetcount>=0:
                message=sendmessage("+15084104311",tweet)
                print message
    else:
        print "no notifications sent"

def mainbackend():
    #Pupulate any new neighborhoods
    for neighborhood in Karachineighborhoodlist:
        populateneighborhood(neighborhood)
    #Get Latest TweetID from DB
    tweets = GetTweets()
    latesttweetid = getlatesttweetid()
    print latesttweetid
    #Start searching after latesttweetID
    for hashtag in hashtags:
        allparsedtweets = tweets.getparsedtweetsforsearctterm(hashtag, 200, latesttweetid)
        allunparsedtweets = tweets.getunparsedtweetsforsearctterm(hashtag, 200, latesttweetid)

        print 'length of parsed tweets for %s = %s' % (hashtag, allparsedtweets.__len__())
        print 'length of unparsed tweets for %s = %s' %(hashtag, allunparsedtweets.__len__())

        for tweet in allparsedtweets:
                text = tweet.text
                createdtime = tweet.created_at
                userid = tweet.user.id
                userscreenname = tweet.user.screen_name
                isretweet = tweet.retweeted + checkforretweet(tweet)
                RetweetCount = tweet.retweet_count
                userlocation = tweet.user.location
                tweetid = tweet.id
                userfollowers = tweet.user.followers_count
                tweetlocation = tweet.geo
                populatedb(text, createdtime, userid, userscreenname, isretweet, RetweetCount, userlocation, tweetid, userfollowers, tweetlocation)
                #sendnotifications(text,RetweetCount,userfollowers)


