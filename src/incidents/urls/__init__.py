from django.urls import path, include

urlpatterns = [
    path('', include('incidents.urls.support_requests')),
    path('', include('incidents.urls.jobs')),
]
