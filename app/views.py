from django.shortcuts import render, redirect, get_list_or_404
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'app/todos.html', {'todos': todos})