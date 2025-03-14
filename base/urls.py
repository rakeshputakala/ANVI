from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('user_registration', user_registration, name='user_registration'),
    path('user_login', user_login, name='user_login'),
    path('upload_file', upload_file, name='upload_file'),
    path('files', file_list, name='file_list'),
    path('files/<int:pk>', interact_with_single_file, name='single_file'),
    path('user_register', user_registration, name='user_register'),
    path('user_login', user_login, name='user_login'),
    path('user_logout', user_logout, name='user_logout')
]
