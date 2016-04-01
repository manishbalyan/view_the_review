from django.conf.urls import patterns, url
from vtr import views


urlpatterns = patterns('', url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^add_query/$', views.add_query, name='add_query'),
    url(r'^branchcs/$', views.branchcs, name='branchcs'),
    url(r'^branchit/$', views.branchcs, name='branchit'),
    url(r'^branchec/$', views.branchcs, name='branchec'),
    url(r'^branchme/$', views.branchcs, name='branchme'),
    url(r'^branchee/$', views.branchcs, name='branchee'),
    url(r'^branchce/$', views.branchcs, name='branchce'),
    url(r'^(?P<slug>[\w|\-]+)/$', views.query, name='query'),

)
