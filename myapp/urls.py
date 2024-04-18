from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name= "index"),
    path('creatorName/', views.myName, name= "about"),
    path('hello/', views.helloWorld),
    path('projects/', views.project, name= "projects"),
    path('task/', views.task, name= "tasks"),
    path('tasks/create_task/', views.create_task, name= "create_tasks"),
    path('create_project', views.create_projects, name= "create_projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
]
