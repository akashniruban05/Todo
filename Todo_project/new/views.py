from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def addtask(request):
    task = request.POST['task']
    Task.objects.create(Task=task)
    return redirect('home')