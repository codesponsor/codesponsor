from django.conf.urls import url
from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.mail, name='index')
]
