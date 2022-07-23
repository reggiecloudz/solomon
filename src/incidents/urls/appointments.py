from django.urls import include, path

from incidents.views import appointment_collection, appointment_detail, appointment_response

urlpatterns = [
    path('api/appointments/', include(([
        path('', appointment_collection, name='appointment_collection'),
        path('<int:pk>/', appointment_detail, name='appointment_detail'),
        path('<int:pk>/response/', appointment_response, name='appointment_response'),
    ], 'appointment'))),
]
