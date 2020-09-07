from django.contrib import admin
from .models import Photo, Project, VideoSettings, WebsiteSettings

# Register your models here.

admin.site.register(Project)
admin.site.register(VideoSettings)
admin.site.register(WebsiteSettings)
admin.site.register(Photo)
