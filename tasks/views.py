from django.shortcuts import render
from . import models, forms

def index(request):
    tasks = models.Task.objects.all()
    form = forms.TaskForm()
    return render(request, 'tasks/lists.html', {'tasks': tasks, 'form': form})