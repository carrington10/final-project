from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "home.html" ## can replace as index
