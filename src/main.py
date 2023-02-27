from django.shortcuts import redirect, render
from app.models import TodoList

def home(request):
    
    tasks = TodoList.objects.all()
    context = {'tasks': tasks}

    return render(request, 'index.html', context)