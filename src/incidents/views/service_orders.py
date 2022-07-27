from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from accounts.models import Client
from assets.models.device import Device
from incidents.models import ServiceOrder
from incidents.serializers import ServiceOrderSerializer

# /api/service_orders/device/{pk}
@api_view(['GET', 'POST'])
def device_service_order_collection(request, pk):
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        service_orders = ServiceOrder.objects.filter(device=device)
        serializer = ServiceOrderSerializer(service_orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'problem': request.data.get('problem'),
            'device': device.pk,
            'client': device.client.pk,
        }
        serializer = ServiceOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /api/service_orders
@api_view(['GET'])
def service_order_collection(request):
    if request.method == 'GET':
        service_orders = ServiceOrder.objects.all()
        serializer = ServiceOrderSerializer(service_orders, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def client_service_order_collection(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        service_orders = ServiceOrder.objects.filter(client=client)
        serializer = ServiceOrderSerializer(service_orders, many=True)
        return Response(serializer.data)

# /api/service_orders/{pk}
@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def service_order_detail(request, pk):
    try:
        service_order = ServiceOrder.objects.get(pk=pk)
    except ServiceOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServiceOrderSerializer(service_order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServiceOrderSerializer(service_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = ServiceOrderSerializer(service_order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        service_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
def change_service_order_status(request, pk):
    try:
        service_order = ServiceOrder.objects.get(pk=pk)
    except ServiceOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PATCH':
        data = {
            "status": request.data.get('status')
        }
        serializer = ServiceOrderSerializer(service_order, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def make_offer(request, pk):
    try:
        service_order = ServiceOrder.objects.get(pk=pk)
    except ServiceOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PATCH':
        data = {
            "offer": request.data.get("offer")
        }
        serializer = ServiceOrderSerializer(service_order, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def offer_response(request, pk):
    try:
        service_order = ServiceOrder.objects.get(pk=pk)
    except ServiceOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PATCH':
        data = {
            "response": request.data.get("response")
        }
        serializer = ServiceOrderSerializer(service_order, data=data, partial=True)
        if serializer.is_valid():
            service_order.offer["response"] = data['response']
            service_order.save()
            # serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)