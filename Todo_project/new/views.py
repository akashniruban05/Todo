from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

# Create your views here.
def addtask(request):
    task = request.POST['task']
    Task.objects.create(Task=task)
    return redirect('home')

def done(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.Is_finished = True
    task.save()
    return redirect('home')
    
def undone(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.Is_finished=False
    task.save()
    return redirect('home')

def edit(request,pk):
    get_task = get_object_or_404(Task,pk=pk)
    if request.method == "POST":
        new = request.POST['task']
        get_task.Task = new
        get_task.save()
        return redirect('home')
    else:
        context = {
            "get_task":get_task
            }
    return render(request,'edit.html',context) 

def delete(request,pk):
    delete_task = get_object_or_404(Task,pk=pk)
    delete_task.delete()
    return redirect('home')