from django.test import TestCase
from django.urls import reverse

from tasks.models import Task


class TaskModelTest(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(
            content="Learn Django"
        )
        self.assertEqual(task.content, "Learn Django")
        self.assertEqual(Task.objects.count(), 1)

    def test_task_update(self):
        task = Task.objects.create(
            content="Learn Python"
        )
        task.content = "Learn Django"
        task.save()
        task.refresh_from_db()
        self.assertEqual(task.content, "Learn Django")

    def test_task_delete(self):
        task = Task.objects.create(
            content="Learn Django"
        )
        task.delete()
        self.assertEqual(Task.objects.count(), 0)


class TaskListViewTest(TestCase):
    def test_task_list_view(self):
        Task.objects.create(
            content="Learn Django"
        )
        response = self.client.get(
            reverse("tasks:task-list")
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Learn Django")


class TaskToggleStatusTest(TestCase):
    def test_toggle_task_status(self):
        task = Task.objects.create(
            content="Learn Django"
        )
        self.assertFalse(task.is_done)
        response = self.client.post(
            reverse("tasks:task-toggle", args=[task.pk])
        )
        task.refresh_from_db()
        self.assertTrue(task.is_done)
        self.assertRedirects(
            response,
            reverse("tasks:task-list")
        )

    def test_toggle_task_status_back(self):
        task = Task.objects.create(
            content="Learn Django",
            is_done=True
        )
        self.client.post(
            reverse("tasks:task-toggle", args=[task.pk])
        )
        task.refresh_from_db()
        self.assertFalse(task.is_done)
