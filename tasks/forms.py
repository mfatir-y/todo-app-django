from django import forms
from django.forms import ModelForm
from . import models

class TaskForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task', 'style': "padding: 0.3rem 1rem; border-radius: 0.5rem; margin: 1rem 0;"}))

    class Meta:
        model = models.Task
        fields = "__all__"
