from django.conf.urls import patterns, url
from probtune import views

urlpatterns = patterns('', url(r'^add_queryP', views.add_queryP, name='add_queryP'),
	url(r'^probQS', views.probQS, name='probQS'),
	url(r'^probQF', views.probQF, name='probQF'),
	url(r'^my_probQF', views.my_probQF, name='my_probQF'),
	url(r'^my_probQS', views.my_probQS, name='my_probQS'),
	url(r'^(?P<slug>[\w|\-]+)/$', views.probquery, name='probquery'),
    url(r'^my_probQF/(?P<slug>[\w|\-]+)/$', views.probquery, name='probquery'),
    url(r'^my_probQS/(?P<slug>[\w|\-]+)/$', views.probquery, name='probquery'),
)