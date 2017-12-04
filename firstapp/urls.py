from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^main', views.main, name='main'),
    url(r'^introduce', views.introduce, name='introduce'),
    url(r'^study', views.study, name='study'),
    
    url(r'^base', views.base, name='base'),
    url(r'^post/(?P<post_id>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/new', views.post_new, name='post_new'),
    url(r'^$', views.post_list, name='post_list'),
    ]
