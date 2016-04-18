from django.conf.urls import patterns, url
from vtr import views


urlpatterns = patterns('', url(r'^$', views.home, name='home'),
    url(r'^registerS/$', views.registerS, name='registerS'),
    
    #url(r'^search_page/$', views.search_page, name='search_page'),
    url(r'^add_queryS/$', views.add_queryS, name='add_queryS'),
    url(r'^my_query/$', views.my_query, name='my_query'),
    url(r'^week/$', views.week, name='week'),
    url(r'^month/$', views.month, name='month'),
    url(r'^views/$', views.views, name='views'),
    url(r'^comment/$', views.comment, name='comment'),
    url(r'^(?P<slug>[\w|\-]+)/$', views.query, name='query'),
    #url(r'^query/(?P<slug>[\w|\-]+)/$', views.query, name='query'),
    url(r'^branch/(?P<branch_name>\w+)/$', views.branch, name='branch'),
    
)
