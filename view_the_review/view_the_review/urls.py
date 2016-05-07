"""Imports for view_the_review Apps."""
from django.conf.urls import include, url
from django.contrib import admin
from settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'vtr.views.home', name='home'),
    url(r'^search/$', include('haystack.urls')),
    url(r'^confirm/(?P<activation_key>\w+)/', ('vtr.views.register_confirm')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'vtr/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}, name='logout'),
    url(r'^vtr/', include('vtr.urls')),
    url(r'^hostel/', include('hostel.urls')),
    url(r'^faculty/', include('faculty.urls')),
    url(r'^probtune/', include('probtune.urls')),
    url(r'^administration/', include('administration.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    url(r'^comments/', include('fluent_comments.urls')),
]
