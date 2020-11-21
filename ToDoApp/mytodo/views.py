from django.shortcuts import render, redirect
from django.http import HttpResponse
from mytodo.models import ToDo
from mytodo.forms import ToDoForm

# Create your views here.
def home(request):
    template_name = 'home.html'
    todo_list = ToDo.objects.all() # returns queryset
    form = ToDoForm()
    # print(todo_list)
    context = {'app_name': "ToDo App", 'todo_list': todo_list, 'form': form}
    return render(request, template_name, context=context)

def add_todo(request):
    if request.method == 'POST':
        # save the todo
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo_text = form.cleaned_data.get('todo_text')
            ToDo.objects.create(todo_text=todo_text)
    
    return redirect('home')


def delete_todo(request, todo_id):
    if request.method == 'POST':
        todo_obj = ToDo.objects.get(pk=todo_id)
        todo_obj.delete()

    return redirect('home')


def edit_todo(request, todo_id):
    todo_obj = ToDo.objects.get(pk=todo_id)

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo_obj.todo_text = form.cleaned_data.get('todo_text')
            todo_obj.save()
            return redirect('home')

    template_name = 'edit.html'
    form = ToDoForm(initial={'todo_text': todo_obj.todo_text})
    context = {'app_name': "ToDo App", 'form': form, 'todo_obj': todo_obj}
    return render(request, template_name, context)