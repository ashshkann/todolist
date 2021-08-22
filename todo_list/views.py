from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TodoItem
from .forms import TodoItemForm

# Create your views here.
def todo_views(request):
    user = request.user
    query = TodoItem.objects.filter(owner = user)
    if request.method == 'POST':
        checked_list = request.POST.getlist('checked')
        checked_list = [int(i) for i in checked_list]
        for todo_item in query:
            if todo_item.id in checked_list:
                TodoItem.objects.filter(id = todo_item.id).update(checked=True)
            else:
                TodoItem.objects.filter(id = todo_item.id).update(checked=False)
        return redirect('/todo')

    context = {
        'todolist':query
    }

    return render(request, "todo_views.html", context)


def creat_item(request):
    user = request.user
    if request.method == 'POST':
        form = TodoItemForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit= False)
            instance.owner = user
            instance.save()
            return redirect('/todo')
    form = TodoItemForm()

    context = {
        'form': form
    }
    return render(request, 'creat_todo.html', context)

def delete_item(request, id):
    try:
        item = TodoItem.objects.get(id = id)
    except:
        return redirect('/todo')
    if item.owner == request.user:
        item.delete()
        return redirect('/todo')
    else:
        return redirect('/todo')