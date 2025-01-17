from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'task_manager/index.html')


def add(request):
    return HttpResponse('add task')


def update(request, task_id):
    return HttpResponse(f'update task {task_id}')


def delete(request, task_id):
    return HttpResponse(f'delete task {task_id}')
