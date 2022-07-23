from django.urls import include, path

from incidents.views import implementation_collection, implementation_detail

urlpatterns = [
    path('api/implementations/', include(([
        path('', implementation_collection, name='implementation_collection'),
        path('<int:pk>/', implementation_detail, name='implementation_detail'),
    ], 'implementation'))),
]
