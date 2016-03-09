from django.conf.urls import patterns, url
from vtr import views


urlpatterns = patterns('', url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^add_query/$', views.add_query, name='add_query'),
    url(r'^branchcs/$', views.branchcs, name='branchcs'),
    url(r'^branchec/$', views.branchec, name='branchec'),
    url(r'^branchme/$', views.branchme, name='branchme'),
    url(r'^branchee/$', views.branchee, name='branchee'),
    url(r'^branchit/$', views.branchit, name='branchit'),
    url(r'^branchce/$', views.branchce, name='branchce'),
    url(r'^(?P<slug>[\w|\-]+)/$', views.query, name='query'),
    
)
