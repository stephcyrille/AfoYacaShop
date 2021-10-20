from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.conf import settings

import os

from account.forms import AddEndUserForm
from account.models import Contact
from utils.libs import file_reader

BASE_DIR = settings.BASE_DIR


class LoginView(TemplateView):
    template_name = 'account/login.html'

    def get(self, request, **kwargs):
        try:
            request.session['next'] = None
            request.session['next'] = request.GET.get('next')
        except Exception as e:
            print("Not next parameter", e.__str__())
        return render(request, self.template_name)

    def post(self, request, **kwargs):
        username = request.POST.get('email', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        try:
            next_param = request.session['next']
        except Exception as e:
            print("Not next parameter, we will set it as none", e.__str__())
            next_param = None

        if user is not None and user.is_active:
            login(request, user)
            if next_param:
                # Cleaning session next param
                request.session['next'] = None
                return redirect(next_param)
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


@login_required
def my_orders(request):
    template_name = "account/dashboard/my_orders.html"
    context = {}

    return render(request, template_name, context)


@login_required
def my_box(request):
    try:
        current_plan = request.user.userprofile.plan.name
    except:
        current_plan = ''

    if current_plan:
        if current_plan == 'FREE':
            # TODO Return an unauthorized custom page here
            return redirect(reverse('home'))
        else:
            template_name = "account/dashboard/my_box.html"
            context = {}
            return render(request, template_name, context)
    else:
        return redirect(reverse('home'))


@login_required
def settings(request):
    template_name = "account/dashboard/settings.html"

    contacts_list = Contact.objects.filter(profile=request.user.userprofile, is_archived=False)

    context = {
        "contacts": contacts_list
    }
    return render(request, template_name, context)
