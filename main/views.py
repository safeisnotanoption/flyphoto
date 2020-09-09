from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project, VideoSettings, WebsiteSettings
from .forms import ProjectForm, VideoSettingsForm, WebsiteSettingsForm, PhotoForm


def index(request):
    return render(request, 'main/index.html')


@login_required
def my_projects(request):
    projects = Project.objects.filter(user=request.user).order_by('-id')
    return render(request, 'main/my_projects.html', {'projects': projects})


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
            return redirect(reverse('edit_video', args=(project.id,)))
        else:
            print("form isn't valid")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectForm(label_suffix='', use_required_attribute=False)

    return render(request, 'main/create_project.html', {'form': form})


def get_object_by_project_id(model_object, project_id):
    obj, created = model_object.objects.get_or_create(project_id=project_id)
    return obj


@login_required
def edit_project(request, project_id):
    obj = get_object_by_project_id(Project, project_id)

    if request.user == obj.project.user:
        pass
    else:
        print("You are not owner")
        return redirect('account_login')

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST, request.FILES, instance=obj)
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
        form = ProjectForm(instance=obj)

    return render(request, 'main/edit_project.html', {'form': form, 'project_id': project_id})


@login_required
def edit_video(request, project_id):
    obj = get_object_by_project_id(VideoSettings, project_id)

    if request.user == obj.project.user:
        pass
    else:
        print("You are not owner")
        return redirect('account_login')

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VideoSettingsForm(request.POST, request.FILES, instance=obj)
        # check whether it's valid:
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect(reverse('edit_website', args=(project_id,)))
        else:
            print('form isnt valid')
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = VideoSettingsForm(instance=obj)

    return render(request, 'main/edit_video.html', {'form': form, 'project_id': project_id})


@login_required
def edit_website(request, project_id):
    obj = get_object_by_project_id(WebsiteSettings, project_id)

    if request.user == obj.project.user:
        pass
    else:
        print("You are not owner")
        return redirect('account_login')

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WebsiteSettingsForm(request.POST, request.FILES, instance=obj)
        # check whether it's valid:
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('my_projects')
        else:
            print('form isnt valid')
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = WebsiteSettingsForm(instance=obj)

    return render(request, 'main/edit_website.html', {'form': form, 'project_id': project_id})


@login_required
def project_page(request, project_address):
    project = Project.objects.get(address=project_address)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            print('form is valid')
            photo = form.save(commit=False)
            photo.project = project
            photo.save()
            return HttpResponse("Ваша фотография успешно загружена!")

    else:
        form = PhotoForm()
    return render(request, 'main/project_page.html', {'project': project, 'form': form,
                                                      'project_address': project_address})


def contacts(request):
    return render(request, 'main/contacts.html')
