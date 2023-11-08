from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('_apps.website.urls', 'website'), namespace='website')),
    path('auth/', include(('_apps.website.auth_urls', 'auth'), namespace='auth')),
]
