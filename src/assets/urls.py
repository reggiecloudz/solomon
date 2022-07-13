from django.urls import include, path

from .views import add_device

urlpatterns = [
    path('devices/', include(([
        path('add/', add_device, name='add_device'),
    ], 'devices'))),
]
