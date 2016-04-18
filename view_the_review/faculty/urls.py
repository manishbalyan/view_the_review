from django.conf.urls import patterns, url
from faculty import views

urlpatterns = patterns('', url(r'^index/$', views.index, name='index'),
    url(r'^registerF/$', views.registerF, name='registerF'),
    #url(r'^search_page/$', views.search_page, name='search_page'),
    url(r'^my_queryf/$', views.my_queryf, name='my_queryf'),
    url(r'^(?P<slug>[\w|\-]+)/$', views.query, name='query'),
    url(r'^my_query/(?P<slug>[\w|\-]+)/$', views.query, name='query'),
    url(r'^branch/(?P<branch_name>\w+)/$', views.branch, name='branch'),
    
)