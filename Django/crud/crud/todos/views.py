from ast import Delete
from shutil import ReadError
from sqlite3 import complete_statement
from turtle import update
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all().order_by("priority")
    context = {
        "todos" : todos,
    }
    return render(request, 'todos/index.html', context)

def create(request):
    
    todo = request.GET
    v_list = []
    for i in todo:
        v_list.append(todo[i])

    Todo.objects.create(content=v_list[0], priority=v_list[1], deadline=v_list[2])
    return redirect('todos:index')

def update(request, todo_pk):
    todo = Todo.objects.get(id = todo_pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todos:index')

def delete(request, todo_pk):
    todo = Todo.objects.get(id = todo_pk)
    todo.delete()
    return redirect('todos:index')

def detail(request, pk_):
    # get() 메소드를 사용해서 특정 pk의 데이터를 불러옴
    # 불러온 데이터를 변수에 할당
    todo = Todo.objects.get(pk = pk_)
    context = {
        'todo' : todo,
    }
    return render(request, 'todos/detail.html', context)

def edit(request, pk_):
    todo = Todo.objects.get(pk = pk_)
    context = {
        'todo' : todo,
    }
    return render(request, 'todos/edit.html', context)

def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.complete_
    todo.save()
    return redirect('articles:detail', todo.pk)