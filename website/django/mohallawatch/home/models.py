from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.

class TwitterUser(models.Model):
    #__tablename__ = "user"
    user_id = models.IntegerField(primary_key=True, db_column='id')
    username = models.TextField()
    followerscount = models.IntegerField()

    def __unicode__(self):
            return self.username

    class Meta:
            db_table = 'twitterusers'

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True, db_column='id')
    description = models.TextField()

class Reliability(models.Model):
    reliability_id = models.IntegerField(primary_key=True, db_column='id')
    description = models.TextField()


class Neighborhood(models.Model):
    __tablename__ = "neighborhood"
    id = models.IntegerField(primary_key=True)
    name = models.TextField(primary_key=True)
    radius = models.FloatField()

    def __repr__(self):
        return "<Neighborhood('%s')>" % (self.name.encode('utf8'))

    class Meta:
            db_table = 'neighborhood'


class City(models.Model):
    __tablename__ = "city"
    id = models.IntegerField(primary_key=True)
    name = models.TextField(primary_key=True)
    radius = models.FloatField()

    def __repr__(self):
        return "<City('%s')>" % (self.name.encode('utf8'))

    class Meta:
            db_table = 'city'

class Tweets(models.Model):
    id = models.IntegerField(primary_key=True)
    violentterm = models.IntegerField()
    ishashtag = models.BooleanField()
    isretweet = models.BooleanField()
    retweetcount = models.IntegerField()
    favouritescount = models.IntegerField()
    geo = models.TextField()
    tweettext = models.TextField()
    createddate = models.DateTimeField()
    tweetid = models.BigIntegerField()
    user = models.ForeignKey(TwitterUser)
    city = models.ForeignKey(City)
    category = models.ForeignKey(Category)
    reliability = models.ForeignKey(Reliability)
    class Meta:
        db_table = 'tweet'

    def __unicode__(self):  # Python 3: def __str__(self):
         return self.text

   ##id = models.IntegerField(primary_key=True)
    #name = models.TextField(primary_key=True) # This field type is a guess.
    #latitude = models.TextField(blank=True) # This field type is a guess.
    #longitude = models.TextField(blank=True) # This field type is a guess.
    #earliest_tweet_id = models.IntegerField(null=True, blank=True)
    #latest_tweet_id = models.IntegerField(null=True, blank=True)
    #radius = models.TextField(blank=True) # This field type is a guess.
    #def __unicode__(self):  # Python 3: def __str__(self):
    # return self.name
    #class Meta:
    #    db_table = 'cities'

#class TweetCities(models.Model):
#    city_name = models.IntegerField(null=True, blank=True)
#    tweet_id = models.IntegerField(null=True)
#    class Meta:
#        db_table = 'tweet_cities'










