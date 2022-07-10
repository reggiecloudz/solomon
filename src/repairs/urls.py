from django.urls import include, path

from .views import add_device, add_repair

urlpatterns = [
    path('devices/', include(([
        path('add/', add_device, name='add_device'),
    ], 'devices'))),
     path('repairs/', include(([
        path('add/<int:pk>/', add_repair, name='add_repair'),
    ], 'repairs'))),
]
