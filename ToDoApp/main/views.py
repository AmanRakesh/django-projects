from django.shortcuts import render, HttpResponseRedirect
from django.utils import timezone
from . import models


# Create your views here.
def home(request):
    todo_items = models.Todo.objects.all().order_by("-added_date") # - for getting newest to oldest
    dataToSend = {
        "todo_items": todo_items,
    }
    return render(request, 'main/index.html', dataToSend)

def add_todo(request):
    todo_text = request.POST.get('todo_input')
    current_date = timezone.now()
    created_object = models.Todo.objects.create(added_date = current_date, text = todo_text)
    print(created_object, created_object.id)
    return HttpResponseRedirect('/')


def delete_todo(request, todo_id ):
    models.Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
