from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import  get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404    
from .forms import createNewTask, createNewProject

# Create your views here.

def home_view (request):
    title = 'Welcome to Django course!!'
    return render(request, 'index.html', {
        'title': title
    })

def helloWorld(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" %username)

def myName(request):
    username  = 'Julian Homez'
    return render(request, 'about_creator.html', {
        'username' : username
    })

def project(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects' : projects
    })

def task(request):
    #task = Task.objects.get(title=title)
    task = Task.objects.all()
    return render(request, 'tasks/task.html', {
        'task' : task
    })
    
def create_task (request):
   if request.method == 'GET':
       # show inteface
       return render(request, 'tasks/create_task.html', {
           'form': createNewTask()
       })
   else:
        Task.objects.create(title = request.POST['title'],
                            description = request.POST['description'], project_id=2)
        return redirect('tasks')
    
def create_projects(request):
    if request.method == 'GET':
        # show inteface
        return render(request, 'projects/create_project.html', {
        'form': createNewProject()
    })
    else:
        Project.objects.create(name = request.POST['name'])
        return  redirect('projects')

def project_detail (request, id):
    get_object_or_404(Project, id= id)
    project = Project.objects.get(id=id)
    task = Task.objects.filter(project_id = id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'task': task
    })
        
        

    
