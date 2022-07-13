from django.urls import include, path

from .views import report_incident, review_incident

urlpatterns = [
     path('incidents/', include(([
        path('report/<int:pk>/', report_incident, name='report_incident'),
        path('review/<int:pk>/', review_incident, name='review_incident'),
    ], 'incidents'))),
]
