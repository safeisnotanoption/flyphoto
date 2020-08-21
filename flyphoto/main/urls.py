from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts', views.contacts, name='contacts'),
    path('photo_list', views.photo_list, name='photo_list'),

    path('auth', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token')
]
