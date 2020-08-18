from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts', views.contacts, name='contacts'),
    path('photo_list', views.photo_list, name='photo_list')
]
