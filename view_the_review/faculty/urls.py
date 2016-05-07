"""Imports for faculty urls."""
from django.conf.urls import patterns, url
from faculty import views
from django.views.generic import TemplateView

urlpatterns = patterns('', url(r'^index/$', views.index, name='index'),
    url(r'^registerF/$', views.registerF, name='registerF'),
    url(r'^my_queryf/$', views.my_queryf, name='my_queryf'),
    url(r'^weekf/$', views.weekf, name='weekf'),
    url(r'^monthf/$', views.monthf, name='monthf'),
    url(r'^viewsf/$', views.viewsf, name='viewsf'),
    url(r'^commentf/$', views.commentf, name='commentf'),
    url(r'^(?P<slug>[\w|\-]+)/$', views.query, name='query'),
    url(r'^my_query/(?P<slug>[\w|\-]+)/$', views.query, name='query'),
    url(r'^branch/(?P<branch_name>\w+)/$', views.branch, name='branch'),
    url(r'^tag/(?P<tag>[a-zA-Z0-9-]+)/?$', views.tagf, name='tagf'),
    url(r'^tag_page/$', TemplateView.as_view(template_name='tag_page.html')),
    url(r'^queryf_update/(?P<pk>\d+)$', views.queryf_update, name='queryf_update'),
    url(r'^queryf_delete/(?P<pk>\d+)$', views.queryf_delete, name='queryf_delete'),
    url(r'^commentf_delete/(?P<pk>\d+)$', views.commentf_delete, name='commentf_delete')
)
