from django.contrib import admin
#from home.models import City, Neighborhood, Tweet
from models import City, Tweets

__author__ = 'hkapadia'

admin.site.register(City)
#admin.site.register(Neighborhood)
admin.site.register(Tweets)

