from main.models import Project, VideoSettings, WebsiteSettings
from main.forms import ProjectForm, VideoSettingsForm, WebsiteSettingsForm
VideoSettings
from django.shortcuts import render, redirect, reverse, get_object_or_404
VideoSettings.objects.get_or_create(project__pk=1)