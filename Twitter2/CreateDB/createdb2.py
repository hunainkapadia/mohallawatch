__author__ = 'hkapadia'
#To create db run python createdb2.py from command line

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,backref,sessionmaker
import os

db = create_engine('sqlite:///../CreateDB/tutorial1.db', echo=False, )
Session = sessionmaker(bind=db)
Base = declarative_base()
session = Session()


class City(Base):
    __tablename__ = "city"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    radius = Column(Float)

    def __repr__(self):
        return "<City('%s')>" % (self.name.encode('utf8'))

class Neighborhood(Base):
    __tablename__ = "neighborhood"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    radius = Column(Float)

    def __repr__(self):
        return "<Neighborhood('%s')>" % (self.name.encode('utf8'))


class TwitterUser(Base):
    __tablename__ = 'twitterusers'
    id = Column(Integer, primary_key=True)
    username = Column(UnicodeText)
    location = Column(UnicodeText)
    followerscount = Column(Integer)
    followingcount = Column(Integer)
    totaltweets = Column(Integer)
    lasttweetdate = Column(DateTime)

    def __repr__(self):
        return "<TwitterUser('%s')>" % (self.username.encode('utf-8'))


class Reliability(Base):
    __tablename__= 'reliability'
    id = Column(Integer, primary_key=True)
    description = Column(String)


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    description = Column(String)


class Tweet(Base):
    """"""
    __tablename__ = "tweet"

    id = Column(Integer, primary_key=True)
    violentterm = Column(Integer)
    ishashtag = Column(Boolean)
    isretweet = Column(Boolean)
    retweetcount = Column(Integer)
    favouritescount = Column(Integer)
    geo = Column(UnicodeText)
    tweettext = Column(UnicodeText)
    createddate = Column(DateTime)
    tweetid = Column(BIGINT)
    user_id = Column(Integer, ForeignKey('twitterusers.id'))
    city_id = Column(UnicodeText, ForeignKey('city.id'))
    category_id = Column(Integer, ForeignKey('category.id'))
    reliability_id = Column(Integer, ForeignKey('reliability.id'))

    twitteruser = relationship("TwitterUser", backref=backref('twitterusers'))
    city = relationship("City", backref=backref('city'))
    category = relationship("Category", backref=backref('category'))
    reliability = relationship("Reliability", backref=backref('reliability'))

    def __repr__(self):
        return "<Tweet('%s')>" % (self.text.encode('utf8'))


Base.metadata.create_all(db)


def create_tables():
    Base.metadata.create_all(db)





