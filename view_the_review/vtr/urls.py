from django.conf.urls import patterns, url
from vtr import views


urlpatterns = patterns('', url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^add_query/$', views.add_query, name='add_query'),
    url(r'^(?P<slug>[\w|\-]+)/$', views.query, name='query'),
)
