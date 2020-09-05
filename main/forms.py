from PIL import Image
from django import forms
from django.core.files import File
from .models import Project, VideoSettings, WebsiteSettings
from django.forms import ModelForm, Textarea, TextInput


class ProjectForm(forms.ModelForm):
    """Проекты и их настройки"""
    class Meta:
        model = Project
        fields = ('project_name', 'num_of_participants', 'date', 'time', 'email')


class VideoSettingsForm(forms.ModelForm):
    """Настройки видео"""
    class Meta:
        model = VideoSettings
        fields = ('blend_mode', 'fly_mode', 'final_shot')


class WebsiteSettingsForm(forms.ModelForm):
    """Настройки веб-страницы"""
    class Meta:
        model = WebsiteSettings
        fields = ('address', 'logo', 'header_color', 'background_color')
