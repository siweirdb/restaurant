from django.shortcuts import render
from django.views.generic.base import TemplateView


def send_email(request):
    return


class IndexView(TemplateView):
    template_name = 'templates/index.html'

