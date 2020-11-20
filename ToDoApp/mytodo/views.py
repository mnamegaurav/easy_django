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
        todo_text = request.POST.get('todo_text')
        ToDo.objects.create(todo_text=todo_text)
        return redirect('home')