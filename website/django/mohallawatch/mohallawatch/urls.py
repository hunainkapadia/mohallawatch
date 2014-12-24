from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from hitcount.views import update_hit_count_ajax


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^', include('home.urls', namespace="home")),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^accounts/', include('registration.backends.default.urls')),
     #url(r'^home/ajax/hit/$', update_hit_count_ajax, name='hitcount_update_ajax'),
     )

urlpatterns += staticfiles_urlpatterns()
