from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects.html", context)


def singleproject(request, pk):
    projectobj = Project.objects.get(id=pk)
    return render(request, "projects/single-project.html", {"project": projectobj})


def createproject(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"proform": form}
    return render(request, "projects/project-form.html", context)


def updateproject(request, pk, pin):
    projectobj = Project.objects.get(id=pk)
    form = ProjectForm(instance=projectobj)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=projectobj)
        if form.is_valid():
            form.save()
            if pin == 1:
                return redirect("singleproject", pk)
            else:
                return redirect("projects")

    context = {"proform": form}
    return render(request, "projects/project-form.html", context)


def deleteproject(request, pk, pin):
    projectobj = Project.objects.get(id=pk)
    if request.method == "POST":
        projectobj.delete()
        return redirect("projects")
    context = {"object": projectobj, "pin": int(pin)}
    return render(request, "projects/delete.html", context)


def test(request):
    return HttpResponse(request, "<h1>This is just test </h1>")
