from django.shortcuts import render
from new.models import Task 

def home(request):
    task = Task.objects.filter(Is_finished=False).order_by('updated_at')
    context = {
        "task":task
    }

    return render(request,'home.html',context)