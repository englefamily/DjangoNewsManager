from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('ynet', views.serve_ynet),
    path('create_post/', views.Create_post.as_view(), name='create_post'),
    path('posts_list/', views.List_post, name='posts_list'),
    path('edit_post/<str:id_>', views.edit_post, name='edit_post'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.create_user, name='signup'),
    path('token/', obtain_auth_token),
    path('test/', views.auth_test, name='test'),
    path('', views.base, name='base'),
    path('access_denied/<str:perm_name>', views.no_perms, name='access_denied')
]