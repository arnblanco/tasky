from django.urls import path
from .views import *

urlpatterns = [
    path('', website_home, name='home')
]
