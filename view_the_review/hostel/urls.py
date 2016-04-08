from django.conf.urls import patterns, url
from hostel import views

urlpatterns = patterns('', url(r'^add_queryH', views.add_queryH, name='add_queryH'),
	url(r'^hostelQ', views.hostelQ, name='hostelQ'),
	url(r'^my_hostelQ', views.my_hostelQ, name='my_hostelQ'),
	url(r'^(?P<slug>[\w|\-]+)/$', views.hostelquery, name='hostelquery'),
    url(r'^my_hostelQ/(?P<slug>[\w|\-]+)/$', views.hostelquery, name='hostelquery'),
)