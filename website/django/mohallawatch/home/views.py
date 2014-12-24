# Create your views here.
from django.shortcuts import render, get_object_or_404
#from home.models import City, Neighborhood, Tweet
from models import City, Tweets, TwitterUser, Neighborhood
#from home.forms import Cityform, Neighborhoodform
from forms import Cityform
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
#from datetime import datetime
from django.forms.models import modelformset_factory


def index(request):
    tweet_list=None
    City_list = City.objects.all()
    Neighborhood_list = Neighborhood.objects.all()
    #### NEW CODE ####
    if request.session.get('last_visit'):
        # The session has a value for the last visit
        last_visit_time = request.session.get('last_visit')
        visits = request.session.get('visits', 0)

        if (datetime.datetime.now() - datetime.datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).days > 0:
            request.session['visits'] = visits + 1
            request.session['last_visit'] = str(datetime.datetime.now())
    else:
        # The get returns None, and the session does not have a value for the last visit.
        request.session['last_visit'] = str(datetime.datetime.now())
        request.session['visits'] = 1
    #### END NEW CODE ####
    sessioncount = request.session.get('visits')
    if request.method == 'POST':
        cityname = request.POST['city']
        neighborhoodname = request.POST['neighborhood']
        sinceunicode = request.POST['daysago']
        since = int(sinceunicode)
        startdate = datetime.date.today()
        enddate = startdate - datetime.timedelta(days=since)
        if neighborhoodname == 'All':
            tweet_list = Tweets.objects.filter(isretweet=0, createddate__range=[enddate, startdate]).exclude(tweettext__startswith='RT').order_by('-createddate')
        else:
            tweet_list = Tweets.objects.filter(isretweet=0, tweettext__contains=neighborhoodname, createddate__range=[enddate, startdate]).exclude(tweettext__startswith='RT').order_by('-createddate')
        totaltweetcountforcity = Tweets.objects.count
        context = {'City_list' : City_list,'tweetlist' : tweet_list,
                   'totaltweetcountforcity' : totaltweetcountforcity, 'Neighborhood_list' : Neighborhood_list, 'Session_count' : sessioncount}
        return render(request,'home/search_filter.html', context)
    else:
        context = {'City_list' : City_list, 'Neighborhood_list' : Neighborhood_list, 'Session_count' : sessioncount}
        return render(request,'home/search_filter.html', context)


def detail(request, city_id):
    if request.method == 'POST':
        #form = Neighborhoodform(request.POST or None)
        print 'got in'
        #city = Cities.objects.get(Cities, pk=city_id)
        #neighborhood = Neighborhood.objects.get(Neighborhood_id=neighborhood_id)
    return HttpResponseRedirect(reverse('home:results', args={1,}))


def results(request):
    form = Cityform(request.POST or None)
    cityname = request.POST['city']
    print(cityname)
    listoftweetids = TweetCities.objects.filter(city_name__contains=cityname).values()
    print(listoftweetids.values('tweet_id'))
    tweet_list = Tweets.objects.filter(id__in = listoftweetids.values('tweet_id'))
    print(tweet_list)
    return render(request, 'home/results.html', {'tweetlist' : tweet_list.values('text', 'date')})

def about(request):
    return render(request, 'home/about.html')

def login(request):
    return render(request, 'home/about.html')

