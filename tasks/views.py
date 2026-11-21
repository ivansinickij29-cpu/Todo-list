from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from tasks.models import Task, Tag


class TaskListView(ListView):
    model = Task
    ordering = ["is_done", "-datetime"]
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(CreateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


@require_POST
def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save(update_fields=["is_done"])
    return redirect("tasks:task-list")


class TagListView(ListView):
    model = Tag
    ordering = ["name"]


class TagCreateView(CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
