from django.urls import include, path

from .resources import client_device_collection, device_detail, device_collection

urlpatterns = [
    path('api/devices/', include(([
        path('', device_collection, name='device_collection'),
        path('<int:pk>/', device_detail, name='device_detail'),
        path('client/<str:pk>/', client_device_collection, name='client_device_collection'),
    ], 'devices'))),
    # path('devices/', include(([
    #     path('add/', add_device, name='add_device'),
    # ], 'devices'))),
]
