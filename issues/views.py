from django.shortcuts import render, get_object_or_404
from .models import Task


# Create your views here.

def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'issues/index.html', context)


def show_details(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    context = {'task': task}
    return render(request, 'issues/show_details.html', context)
