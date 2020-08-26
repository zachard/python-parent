"""定义learing_logs的URL模式"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/topics', views.topics, name='topics'),
    path('/new_topic', views.new_topic, name='new_topic'),
    # path('/new_entry/(?P<topic_id>[^/]+)$', views.new_entry, name='new_entry'),
]