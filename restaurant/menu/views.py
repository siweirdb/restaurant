from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


def send_email(request):
    message = request.POST.get('message')
    name = request.POST.get('name')
    subject = f'Резервация стола на {name}'
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['abdullovadlet@gmail.com'],
            fail_silently=False,
        )
        return HttpResponse("Message was successfully sent")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")



class IndexView(TemplateView):
    template_name = 'menu/index.html'
