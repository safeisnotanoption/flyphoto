from PIL import Image
from django import forms
from django.core.files import File
from .models import Project, VideoSettings, WebsiteSettings, Photo
from django.forms import ModelForm, Textarea, TextInput


class ProjectForm(forms.ModelForm):
    """Проекты и их настройки"""
    class Meta:
        model = Project
        fields = ('project_name', 'address', 'num_of_participants', 'date', 'time', 'email')
        widgets = {
            'date': TextInput(attrs={'class': 'datepicker'}),
            'time': TextInput(attrs={'class': 'timepicker'}),
        }


class VideoSettingsForm(forms.ModelForm):
    """Настройки видео"""
    class Meta:
        model = VideoSettings
        fields = ('blend_mode', 'fly_mode', 'final_shot')


class WebsiteSettingsForm(forms.ModelForm):
    """Настройки веб-страницы"""
    class Meta:
        model = WebsiteSettings
        fields = ('logo', 'header_color', 'background_color')


class PhotoForm(forms.ModelForm):
    """Загрузчик фотографий"""
    class Meta:
        model = Photo
        fields = ('file',)
