from django.shortcuts import render, redirect
from django.utils import timezone
from . import models


# Create your views here.
def home(request):
    if request.method == 'POST':
        todo_text = request.POST.get('todo_input')
        todo_id = request.POST.get('todo_id')
        todo_item = models.Todo.objects.get(id=todo_id)
        todo_item.text = todo_text
        todo_item.save()
        redirect('/')

    todo_items = models.Todo.objects.all().order_by("-added_date") # - for getting newest to oldest
    dataToSend = {
        "todo_items": todo_items,
    }
    return render(request, 'main/index.html', dataToSend)

def add_todo(request):
    todo_text = request.POST.get('todo_input')
    current_date = timezone.now()
    created_object = models.Todo.objects.create(added_date = current_date, text = todo_text)
    return redirect('/')

def edit_todo(request, todo_id):
    todo_item = models.Todo.objects.get(id=todo_id)
    todo_text = todo_item.text
    dataToSend = {
        "todo_text": todo_text,
        "todo_id": todo_id,
    }
    return render(request, 'main/update_task.html', dataToSend)

def delete_todo(request, todo_id):
    models.Todo.objects.get(id=todo_id).delete()
    return redirect('/')
