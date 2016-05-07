"""Import for probtune urls."""
from django.conf.urls import patterns, url
from probtune import views

urlpatterns = patterns('', url(r'^add_queryP', views.add_queryP, name='add_queryP'),
    url(r'^probQS', views.probQS, name='probQS'),
    url(r'^probQF', views.probQF, name='probQF'),
    url(r'^my_probQF', views.my_probQF, name='my_probQF'),
    url(r'^my_probQS', views.my_probQS, name='my_probQS'),
    url(r'^weekps/$', views.weekps, name='weekps'),
    url(r'^monthps/$', views.monthps, name='monthps'),
    url(r'^viewsps/$', views.viewsps, name='viewsps'),
    url(r'^commentps/$', views.commentps, name='commentps'),
    url(r'^weekpf/$', views.weekpf, name='weekpf'),
    url(r'^monthpf/$', views.monthpf, name='monthpf'),
    url(r'^viewspf/$', views.viewspf, name='viewspf'),
    url(r'^commentpf/$', views.commentpf, name='commentpf'),
    url(r'^(?P<slug>[\w|\-]+)/$', views.probquery, name='probquery'),
    url(r'^my_probQF/(?P<slug>[\w|\-]+)/$', views.probquery, name='probquery'),
    url(r'^my_probQS/(?P<slug>[\w|\-]+)/$', views.probquery, name='probquery'),
    url(r'^tagp/(?P<tag>[a-zA-Z0-9-]+)/?$', views.tagp, name='tagp'),
    url(r'^queryp_update/(?P<pk>\d+)$', views.queryp_update, name='queryp_update'),
    url(r'^commentp_delete/(?P<pk>\d+)$', views.commentp_delete, name='commentp_delete'),
    url(r'^queryp_delete/(?P<pk>\d+)$', views.queryp_delete, name='queryp_delete'),

)
