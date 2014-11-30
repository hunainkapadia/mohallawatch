__author__ = 'hkapadia'

from django.conf.urls import patterns, url, include

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^results/', views.results, name='results'),
    url(r'^about/', views.about, name='about'),
    #url(r'^registration/$', views.login, {'template_name': 'registration/login.html'}, name='login'),
    #url(r'^registration/', include('registration.backends.default.urls'))
    #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
