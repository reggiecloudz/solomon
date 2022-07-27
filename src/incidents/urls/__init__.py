from django.urls import path, include

urlpatterns = [
    path('', include('incidents.urls.service_orders')),
    path('', include('incidents.urls.jobs')),
    path('', include('incidents.urls.appointments')),
    path('', include('incidents.urls.problem_definitions')),
    path('', include('incidents.urls.root_causes')),
    path('', include('incidents.urls.solutions')),
    path('', include('incidents.urls.implementations')),
    path('', include('incidents.urls.evaluations')),
]
