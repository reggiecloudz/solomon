from django.urls import include, path

from incidents.views import root_cause_collection, root_cause_detail

urlpatterns = [
    path('api/root-causes/', include(([
        path('', root_cause_collection, name='root_cause_collection'),
        path('<int:pk>/', root_cause_detail, name='root_cause_detail'),
    ], 'root_cause'))),
]
