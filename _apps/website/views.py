# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth import login

def website_home(request, template='website/home.html'):

	return render(request, template, {})


# #############################################################################
# AUTH VIEWS
# #############################################################################
class RegistrationView(View):
    template_name = 'auth/signup.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('/')  
        
        return render(request, self.template_name, {'form': form})