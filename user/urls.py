from django.urls import path, include
from .views import *

app_name = 'user'
urlpatterns = [
    path('login/', UsersLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UsersLoginView.as_view(), name='profile'),
    path('segurity/', UsersLoginView.as_view(), name='segurity'),
    path('edit_profile/', UsersLoginView.as_view(), name='edit_profile'),
]
