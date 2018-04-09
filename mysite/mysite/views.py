from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.shortcuts import render, redirect


def login_redirect(request):
            return redirect('/accounts/login')

 ## can replace as index
