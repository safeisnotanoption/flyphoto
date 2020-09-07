from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_project', views.create_project, name='create_project'),
    # path('edit_project/<int:project_id>', views.edit_project, name='edit_project'),
    path('edit_video/<int:project_id>', views.edit_video, name='edit_video'),
    path('contacts', views.contacts, name='contacts'),
]
