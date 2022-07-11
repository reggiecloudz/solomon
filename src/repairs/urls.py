from django.urls import include, path

from .views import add_device, request_repair, review_repair

urlpatterns = [
    path('devices/', include(([
        path('add/', add_device, name='add_device'),
    ], 'devices'))),
     path('repairs/', include(([
        path('request/<int:pk>/', request_repair, name='request_repair'),
        path('review/<int:pk>/', review_repair, name='review_repair'),
    ], 'repairs'))),
]
