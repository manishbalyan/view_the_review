from django.conf.urls import patterns, url
from vtr import views
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('', url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^query/$', views.query, name='query'),
    url(r'^add_query/$', views.add_query, name='add_query'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'vtr/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}, name='logout'),
    
)
