from django.conf.urls import url

from sponsor import views

app_name = 'sponsor'
urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
]
