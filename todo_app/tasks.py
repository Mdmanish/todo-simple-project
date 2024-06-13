from celery import shared_task
from .models import Todo
from django.core.mail import send_mail
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from celery.schedules import crontab
from django.conf import settings


@shared_task
def send_reminder_emails():
    scheduler = BackgroundScheduler()
    scheduler.start()

    upcoming_tasks = Todo.objects.filter(deadline__lte=datetime.now() + timedelta(days=1))

    for task in upcoming_tasks:
        reminder_time = task.deadline - timedelta(hours=1, minutes=15)
        scheduler.add_job(send_reminder_email, "date", run_date=reminder_time, args=[task])
    return "Done"

def send_reminder_email(task):
    subject = f"Reminder: Task '{task.name}' deadline approaching"
    body = f"This is a reminder that your task '{task.name}' is due in 1 hour 15 minutes."
    result = send_mail(
        subject = subject,
        message=body,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[task.user.email],
        fail_silently=True,
    )
    return "Email sent!"
