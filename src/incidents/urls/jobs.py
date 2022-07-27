from django.urls import include, path

from incidents.views import job_collection, job_detail, sevice_order_job_collect

urlpatterns = [
    path('api/jobs/', include(([
        path('', job_collection, name='job_collection'),
        path('<int:pk>/', job_detail, name='job_detail'),
        path('service-order/<int:pk>/', sevice_order_job_collect, name='sevice_order_job_collect'),
    ], 'job'))),
]
