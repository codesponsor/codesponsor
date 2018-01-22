from django.conf.urls import url
from track import views

app_name = 'track'
urlpatterns = [
    url(r'^c/(?P<token>[\w\-]+)/$', views.track_click, name='track_click'),
]