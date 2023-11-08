from django.contrib.auth import views as auth_views
from django.urls import path

from .views import RegistrationView


urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name="auth/login.html", success_url='/app'), name='login'),
    path('signup', RegistrationView.as_view(), name='signup'),
]
