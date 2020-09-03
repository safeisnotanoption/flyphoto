from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit_project', views.edit_project, name='edit_project'),
    path('contacts', views.contacts, name='contacts'),
]
