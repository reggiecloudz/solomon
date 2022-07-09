from django.urls import include, path

from .views import add_device, add_issue

urlpatterns = [
    path('devices/', include(([
        path('add/', add_device, name='add_device'),
    ], 'devices'))),
     path('issues/', include(([
        path('add/<int:pk>/', add_issue, name='add_issue'),
    ], 'issues'))),
]
