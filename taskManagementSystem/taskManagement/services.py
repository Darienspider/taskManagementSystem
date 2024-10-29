from .models import Notification
from django.core.mail import send_mail
from taskManagementSystem.settings import *

def create_notification(user, message, notification_type='info'):
    Notification.objects.create(
        user=user,
        message=message,
        notification_type=notification_type
    )

def send_email_notification(user, subject, message):
    send_mail(
        subject,
        message,
        DEFAULT_FROM_EMAIL,  # set in settings.py
        [user.email],
        fail_silently=False,
    )