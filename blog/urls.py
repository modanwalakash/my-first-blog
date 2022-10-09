from django.conf.urls import url
from . import views
""" This file includes all the url in the project and its description 
urlpatterns=[
    url(r'^$',views.post_list,name='post_list'),
   url(r'^post/(?P<pk>\d+)/$', views.post_detail, name="post_detail"),
]
