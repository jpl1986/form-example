# howdy/urls.py
from django.conf.urls import url
from helloworld import views

app_name='helloworld'
urlpatterns = [
    #url(r'^$', views.HomePageView.as_view()),
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^yourname/$', views.get_name, name='yourname'),
]
