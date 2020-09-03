from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit_project', views.edit_project, name='edit_project'),
    path('contacts', views.contacts, name='contacts'),
    path('photo_list', views.photo_list, name='photo_list'),
]
