from django.urls import path
from . import views_api


urlpatterns = [
    path('posts_list', views_api.list_post, name='posts_list'),
]
