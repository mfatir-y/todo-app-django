from django.shortcuts import render, redirect
from . import models, forms

def index(request):
    tasks = models.Task.objects.all()
    form = forms.TaskForm()

    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'tasks/lists.html', {'tasks': tasks, 'form': form})