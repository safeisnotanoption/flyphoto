from django.shortcuts import render, redirect
from .forms import ProjectForm


def index(request):
    return render(request, 'main/index.html')


def edit_project(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST, request.FILES, label_suffix='', use_required_attribute=False)
        # check whether it's valid:
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('/edit_project')
        else:
            print("form isn't valid")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectForm(label_suffix='', use_required_attribute=False)

    return render(request, 'main/edit_project.html', {'form': form})


def contacts(request):
    return render(request, 'main/contacts.html')
