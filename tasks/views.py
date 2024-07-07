from django.shortcuts import render
from . import models

def index(request):
    tasks = models.Task.objects.all()
    return render(request, 'tasks/lists.html', {'tasks': tasks})