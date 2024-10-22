from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Todo

def home(request):
    return HttpResponse("Bem-vindo à página inicial!")


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"todos": todos})

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    template_name = "todos/todo_form.html"
    success_url = reverse_lazy("todo_list")

class TodoListView(ListView):
    model = Todo
    template_name = "todos/todo_list.html"
    context_object_name = "todos"

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    template_name = "todos/todo_form.html"
    success_url = reverse_lazy('todo_list')

class TodoCompleteView(UpdateView):
    model = Todo
    fields = []
    success_url = reverse_lazy('todo_list')

    def post(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo, pk=kwargs['pk'])
        todo.finished_at = timezone.now()
        todo.save()
        return redirect(self.success_url)

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todos/todo_confirm_delete.html"
    success_url = reverse_lazy("todo_list")