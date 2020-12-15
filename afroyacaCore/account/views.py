from django.shortcuts import render, redirect
from django.http import *
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

import os

from account.forms import AddEndUserForm
from libs import file_reader

BASE_DIR = settings.BASE_DIR


class LoginView(TemplateView):
    template_name = 'account/login.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)

    def post(self, request, **kwargs):
        username = request.POST.get('email', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
        message = ""

        if user is None:
            message = "Mauvais informations d'authentification"

        context = {
            "message" : message
        }

        return render(request, self.template_name, context)


class RegistrationView(TemplateView):
    template_name = 'account/registration.html'
    file_path = os.path.join(BASE_DIR, 'datas', 'text', 'cgu.txt')
    cgu = file_reader.read_file(file_path)

    def get(self, request, **kwargs):
        form = AddEndUserForm()

        context = {
            "form": form,
            "cgu": self.cgu,
        }
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        if request.method == 'POST':
            form = AddEndUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('signin')
        else:
            form = AddEndUserForm()
        context = {
            'form': form,
            "cgu": self.cgu,
        }

        return render(request, self.template_name, context)
