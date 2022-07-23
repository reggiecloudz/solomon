from django.urls import include, path

from incidents.views import (
    device_support_request_collection, 
    support_request_detail, 
    support_request_collection,
    client_support_request_collection,
    change_support_request_status,
    make_offer,
    offer_response,
)

urlpatterns = [
    path('api/support-requests/', include(([
        path('', support_request_collection, name='support_request_collection'),
        path('<int:pk>/', support_request_detail, name='support_request_detail'),
        path('<int:pk>/update-status/', change_support_request_status, name='change_support_request_status'),
        path('<int:pk>/make-offer/', make_offer, name='make_offer'),
        path('<int:pk>/offer-response/', offer_response, name='offer_response'),
        path('client/<str:pk>/', client_support_request_collection, name='client_support_request_collection'),
        path('device/<int:pk>/', device_support_request_collection, name='device_support_request_collection'),
    ], 'support_request'))),
]
