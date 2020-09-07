from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, VideoSettings, WebsiteSettings
from .forms import ProjectForm, VideoSettingsForm, WebsiteSettingsForm


def index(request):
    return render(request, 'main/index.html')


@login_required
def create_project(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST, request.FILES, label_suffix='', use_required_attribute=False)
        # check whether it's valid:
        if form.is_valid():
            print('form is valid')
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect(reverse('edit_project', args=(project.id,)))
        else:
            print("form isn't valid")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectForm(label_suffix='', use_required_attribute=False)

    return render(request, 'main/create_project.html', {'form': form})


@login_required
def edit_video(request, project_id):
    obj, created = VideoSettings.objects.get_or_create(project_id=project_id)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VideoSettingsForm(request.POST, instance=obj)
        # check whether it's valid:
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect(reverse('edit_video', args=(project_id,)))
        else:
            print('form isnt valid')
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = VideoSettingsForm(instance=obj)

    return render(request, 'main/edit_video.html', {'form': form, 'project_id': project_id})


def contacts(request):
    return render(request, 'main/contacts.html')
