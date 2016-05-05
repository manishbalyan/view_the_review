from django.conf.urls import patterns, url
from hostel import views

urlpatterns = patterns('', url(r'^add_queryH', views.add_queryH, name='add_queryH'),
	url(r'^hostelQ', views.hostelQ, name='hostelQ'),
	url(r'^my_hostelQ', views.my_hostelQ, name='my_hostelQ'),
    url(r'^weekh/$', views.weekh, name='weekh'),
    url(r'^monthh/$', views.monthh, name='monthh'),
    url(r'^viewsh/$', views.viewsh, name='viewsh'),
    url(r'^commenth/$', views.commenth, name='commenth'),
	url(r'^(?P<slug>[\w|\-]+)/$', views.hostelquery, name='query'),
    url(r'^my_hostelQ/(?P<slug>[\w|\-]+)/$', views.hostelquery, name='query'),
    url(r'^tagh/(?P<tag>[a-zA-Z0-9-]+)/?$', views.tagh, name='tagh'),
)