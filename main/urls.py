from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_project', views.create_project, name='create_project'),
    path('my_projects', views.my_projects, name='my_projects'),
    path('edit_video/<int:project_id>', views.edit_video, name='edit_video'),
    path('edit_website/<int:project_id>', views.edit_website, name='edit_website'),
    path('p/<str:project_address>', views.project_page, name='project_page'),
    path('contacts', views.contacts, name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
