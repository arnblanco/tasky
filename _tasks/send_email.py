from celery import shared_task
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template


@shared_task
def send_mail(to, subject, s_template, s_context):
	template = get_template(s_template)
	context = Context(s_context)
	content = template.render(s_context)

	msg = EmailMessage(subject, content, 'team@ducrat.in', to=to)
	msg.content_subtype = 'html'
	msg.send()
	
	return True