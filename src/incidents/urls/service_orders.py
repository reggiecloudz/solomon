from django.urls import include, path

from incidents.views import (
    device_service_order_collection, 
    service_order_detail, 
    service_order_collection,
    client_service_order_collection,
    change_service_order_status,
    make_offer,
    offer_response,
)

urlpatterns = [
    path('api/service-orders/', include(([
        path('', service_order_collection, name='service_order_collection'),
        path('<int:pk>/', service_order_detail, name='service_order_detail'),
        path('<int:pk>/update-status/', change_service_order_status, name='change_service_order_status'),
        path('<int:pk>/make-offer/', make_offer, name='make_offer'),
        path('<int:pk>/offer-response/', offer_response, name='offer_response'),
        path('client/<str:pk>/', client_service_order_collection, name='client_service_order_collection'),
        path('device/<int:pk>/', device_service_order_collection, name='device_service_order_collection'),
    ], 'service_order'))),
]
