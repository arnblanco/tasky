# -*- coding: utf-8 -*-
from django.shortcuts import render

def website_home(request, template='website/home.html'):

	return render(request, template, {})