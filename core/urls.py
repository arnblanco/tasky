from django.urls import path, include
from rest_framework.routers import DefaultRouter

from _apps.tareas.api import TareaViewSet

router = DefaultRouter()
router.register(r'tareas', TareaViewSet)

urlpatterns = [
    path('', include(('_apps.website.urls', 'website'), namespace='website')),
    path('auth/', include(('_apps.website.auth_urls', 'auth'), namespace='auth')),
    path('tareas/', include(('_apps.tareas.urls', 'tareas'), namespace='tareas')),

    path('api/', include(router.urls)),
]
