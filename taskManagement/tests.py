from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task, User
from .forms import TaskEntryForm
from django.contrib.auth.models import User
class TaskModelTest(TestCase):

    def setUp(self):
        # Set up test data for each test
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.task = Task.objects.create(
            title="Test Task",
            description="Test task description",
            status="Incomplete",
            creator=self.user
        )

    def test_task_creation(self):
        # Test that a task can be created
        task = Task.objects.get(title="Test Task")
        self.assertEqual(task.description, "Test task description")

    def test_task_status(self):
        # Test task status field
        task = Task.objects.get(title="Test Task")
        self.assertEqual(task.status, "Incomplete")

    def test_user_association_with_task(self):
        # Test that the user is associated with the created task
        task = Task.objects.get(title="Test Task")
        self.assertEqual(task.creator.username, 'testuser')

class TaskViewTest(TestCase):

    def setUp(self):
        # Set up a user and a task for the test
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.task = Task.objects.create(
            title="Test Task",
            description="Test task description",
            status="Incomplete",
            creator=self.user
        )

    def test_task_list_view(self):
        # Test the task list view
        response = self.client.get(reverse('task_list'))  # Assuming 'task_list' is the URL name for the task list
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'taskManagement/task_list.html')
        self.assertContains(response, "Test Task")

    def test_task_update_view(self):
        # Test the task update view
        response = self.client.get(reverse('update_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'taskManagement/update_task.html')

    def test_redirect_if_not_logged_in(self):
        # Test that a non-authenticated user is redirected to login
        self.client.logout()
        response = self.client.get(reverse('update_task', args=[self.task.id]))
        self.assertRedirects(response, '/login/?next=/tasks/task/update/%d/' % self.task.id)

class TaskFormTest(TestCase):

    def test_valid_form(self):
        data = {
            'title': 'Test Task',
            'description': 'Task description',
            'status': 'Incomplete',
            'due_date': '2024-12-31'
        }
        form = TaskEntryForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'title': '',  # Title is required
            'description': 'Task description',
            'status': 'Incomplete'
        }
        form = TaskEntryForm(data=data)
        self.assertFalse(form.is_valid())