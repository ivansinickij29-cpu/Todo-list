from django.urls import path

from tasks import views
from tasks.views import (TaskListView, TaskCreateView,
                         TaskUpdateView, TaskDeleteView)

app_name = "tasks"
urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/add/", TaskCreateView.as_view(), name="task-add"),
    path("tasks/<int:pk>/edit/", TaskUpdateView.as_view(), name="task-edit"),
    path(
        "tasks/<int:pk>/delete/", TaskDeleteView.as_view(),
        name="task-delete"),
    path(
        "tasks/<int:pk>/toggle/", views.toggle_task_status,
        name="task-toggle"),
    path("tags/", views.TagListView.as_view(), name="tag-list"),
    path("tags/add/", views.TagCreateView.as_view(), name="tag-add"),
    path(
        "tags/<int:pk>/edit/", views.TagUpdateView.as_view(),
        name="tag-edit"),
    path(
        "tags/<int:pk>/delete/", views.TagDeleteView.as_view(),
        name="tag-delete"),
]
