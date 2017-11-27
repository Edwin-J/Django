from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^main', views.main, name='main'),
    url(r'^introduce', views.introduce, name='introduce'),
    url(r'^study', views.study, name='study'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    ]
