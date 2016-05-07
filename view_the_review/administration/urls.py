"""Import for admin urls."""
from django.conf.urls import patterns, url
from administration import views

urlpatterns = patterns('', url(r'^index/$', views.index, name='index'),
    url(r'^hostel/$', views.hostel, name='hostel'),
    url(r'^academic/$', views.academic, name='academic'),
    url(r'^Pquery/(?P<slug>[\w|\-]+)/$', views.Pquery, name='Pquery'),
    url(r'^Hquery/(?P<slug>[\w|\-]+)/$', views.Hquery, name='Hquery'),
    url(r'^Aquery/(?P<slug>[\w|\-]+)/$', views.Aquery, name='Aquery'),
)
