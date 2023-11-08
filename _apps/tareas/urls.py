from django.urls import path
from .views import TareaView

urlpatterns = [
    path('', TareaView.as_view(), name='home')
]