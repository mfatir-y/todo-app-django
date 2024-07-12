from django.shortcuts import render, redirect
from . import models, forms

def index(request):
    tasks = models.Task.objects.all()
    form = forms.TaskForm()

    if request.method == "POST":
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'tasks/lists.html', {'tasks': tasks, 'form': form})

def updateTask(request, pk):
    task = models.Task.objects.get(id=pk)
    form = forms.TaskForm(instance=task)

    if request.method == 'POST':
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'tasks/update_task.html', {'task': task, 'form': form})

def deleteTask(request, pk):
    item = models.Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'tasks/delete_task.html', {'item': item})