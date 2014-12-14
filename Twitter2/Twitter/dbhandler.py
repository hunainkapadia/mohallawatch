__author__ = 'hkapadia'
#Take info from tweets and insert into db
import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Twitter2.CreateDB.createdb2 import Tweet, TwitterUser, Neighborhood
from sqlalchemy import update, insert


db = create_engine('sqlite:///../CreateDB/tutorial1.db',
                   echo=False,)
Base = declarative_base()
DBSession = sessionmaker(bind=db)

#need this to pass since_id to tweepy api
def getlatesttweetid():
    s = DBSession()
    if (s.query(Tweet).order_by('-createddate').first() == None):
        lasttweet = 0
        return lasttweet
    else:
        lasttweet = s.query(Tweet).order_by('-tweetid').first()
        return lasttweet.tweetid


def populatedb(text, tweetcreatedate, userid, userscreenname, isretweet, RetweetCount, userlocation,
               tweetid, userfollowers, tweetlocation):
    s = DBSession()
    t1 = Tweet(tweettext=text, createddate=tweetcreatedate, user_id=userid, tweetid=tweetid, retweetcount=RetweetCount,
               isretweet=isretweet, geo = tweetlocation)
    #If tweet does not exist in db add it. Otherwise don't.
    tweetexists = s.query(Tweet).filter(Tweet.id==tweetid).count()
    if tweetexists is 0:
        s.add(t1)
    #If user does not exist, add.
    t2 = TwitterUser(id=userid, username = userscreenname, followerscount = userfollowers)
    userexists = s.query(TwitterUser).filter(TwitterUser.id==userid).count()
    if userexists is 0:
        s.add(t2)
    else:
    #If user exists, update the users followerscount and other parameters
        stmt = update(TwitterUser).where(TwitterUser.id==userid).values(followerscount=userfollowers)
        s.execute(stmt)
    s.commit()

def populateneighborhood(neighborhood):
    s = DBSession()
    if s.query(Neighborhood).filter(Neighborhood.name==neighborhood).count() is 0:
        stmt = insert(Neighborhood).values(name=neighborhood)
        s.execute(stmt)
        s.commit()

def getalltweets(day):
    s=DBSession()
    current_time = datetime.datetime.now()
    delta = current_time - datetime.timedelta(days=day)
    tweetlist = s.query(Tweet).filter(Tweet.createddate > delta).all()
    return tweetlist



