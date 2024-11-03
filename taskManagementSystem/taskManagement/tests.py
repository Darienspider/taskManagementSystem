from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import Task, Assignment

User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')


class TaskModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task.',
            due_date=timezone.now() + timezone.timedelta(days=1),
            priority='High',
            category='Work',
            creator=self.user,
            status='Incomplete'
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'This is a test task.')
        self.assertEqual(self.task.priority, 'High')
        self.assertEqual(self.task.category, 'Work')
        self.assertEqual(self.task.status, 'Incomplete')
        self.assertEqual(self.task.creator, self.user)

    def test_task_str(self):
        self.assertEqual(str(self.task), 'Test Task')


class AssignmentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task.',
            due_date=timezone.now() + timezone.timedelta(days=1),
            priority='Low',
            category='Personal',
            creator=self.user,
            status='Incomplete'
        )
        self.assignment = Assignment.objects.create(
            task=self.task,
            assigned_user=self.user
        )

    def test_assignment_creation(self):
        self.assertEqual(self.assignment.task, self.task)
        self.assertEqual(self.assignment.assigned_user, self.user)

    def test_assignment_str(self):
        self.assertEqual(str(self.assignment), 'testuser - Test Task')
