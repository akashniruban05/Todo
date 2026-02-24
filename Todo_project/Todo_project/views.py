from django.shortcuts import render
from new.models import Task 

def home(request):
    task = Task.objects.filter(Is_finished=False).order_by('updated_at')
    completed_task = Task.objects.filter(Is_finished=True).order_by('updated_at')
    context = {
        "completed_task":completed_task,
        "task":task,
    }

    return render(request,'home.html',context)