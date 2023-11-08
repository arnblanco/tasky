from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_as_mail(subject, message, email, rc_list):
    send_mail(subject, message, email, rc_list)