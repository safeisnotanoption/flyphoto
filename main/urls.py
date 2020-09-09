from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_project', views.create_project, name='create_project'),
    path('my_projects', views.my_projects, name='my_projects'),
    path('edit_video/<int:project_id>', views.edit_video, name='edit_video'),
    path('edit_website/<int:project_id>', views.edit_video, name='edit_website'),
    path('contacts', views.contacts, name='contacts'),
]
