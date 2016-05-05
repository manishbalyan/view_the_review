from django.conf.urls import patterns, url
from vtr import views
from django.views.generic import TemplateView

urlpatterns = patterns('', url(r'^$', views.home, name='home'),
    url(r'^registerS/$', views.registerS, name='registerS'),

    #url(r'^search_page/$', views.search_page, name='search_page'),
    url(r'^add_queryS/$', views.add_queryS, name='add_queryS'),
    url(r'^my_query/$', views.my_query, name='my_query'),
    url(r'^week/$', views.week, name='week'),
    url(r'^month/$', views.month, name='month'),
    url(r'^views/$', views.views, name='views'),
    url(r'^comment/$', views.comment, name='comment'),
    url(r'^tag_page/$', TemplateView.as_view(template_name='tag_page.html')),
    url(r'^(?P<slug>[\w|\-]+)/$', views.query, name='query'),
    #url(r'^query/(?P<slug>[\w|\-]+)/$', views.query, name='query'),
    url(r'^branch/(?P<branch_name>\w+)/$', views.branch, name='branch'),
    url(r'^tag/(?P<tag>[a-zA-Z0-9-]+)/?$', views.tag, name='tag'),
    url(r'^query_update/(?P<pk>\d+)$', views.query_update, name='query_update'),
    url(r'^comment_update/(?P<pk>\d+)$', views.comment_update, name='comment_update'),
    url(r'^query_delete/(?P<pk>\d+)$', views.query_delete, name='query_delete'),
    url(r'^comment_delete/(?P<pk>\d+)$', views.comment_delete, name='comment_delete')

)
