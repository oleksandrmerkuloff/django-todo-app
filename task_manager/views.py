from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task


def index(request):
    task_list = Task.objects.all()
    return render(request, 'task_manager/index.html', {
        "task_list": task_list
    })


def add(request):
    if request.method == 'POST':
        title = request.POST.get('task-title')
        if title:
            Task.objects.create(title=title)
            return redirect('home')


def update(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.POST.get('task_checkbox') is not None:
        is_completed = True
    else:
        is_completed = False
    task.is_completed = is_completed
    task.save()

    return redirect('home')


def delete(request, task_id):
    return HttpResponse(f'delete task {task_id}')
