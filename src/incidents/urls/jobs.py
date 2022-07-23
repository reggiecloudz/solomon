from django.urls import include, path

from incidents.views import job_collection, job_detail

urlpatterns = [
    path('api/jobs/', include(([
        path('', job_collection, name='job_collection'),
        path('<int:pk>/', job_detail, name='job_detail'),
    ], 'job'))),
]
