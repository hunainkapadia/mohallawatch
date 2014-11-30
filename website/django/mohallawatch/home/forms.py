__author__ = 'hkapadia'

from django import forms
#from home.models import City, Neighborhood
from models import City

class Cityform(forms.ModelForm):
    cities = forms.ModelChoiceField(queryset=City.objects.all())

    class Meta:
        model = City
        #exclude = ['City_text']

#class Neighborhoodform(forms.ModelForm):
#    Neighborhood = forms.ModelChoiceField(queryset=Neighborhood.objects.all())
#    class Meta:
#        model = Neighborhood
#        exclude = ['Neighborhood_text']
