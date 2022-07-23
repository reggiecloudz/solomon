from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from accounts.models import Client
from assets.models.device import Device
from incidents.models import SupportRequest
from incidents.serializers import SupportRequestSerializer

# /api/support_requests/device/{pk}
@api_view(['GET', 'POST'])
def device_support_request_collection(request, pk):
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        support_requests = SupportRequest.objects.filter(device=device)
        serializer = SupportRequestSerializer(support_requests, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'problem': request.data.get('problem'),
            'device': device.pk,
            'client': device.client.pk,
        }
        serializer = SupportRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /api/support_requests
@api_view(['GET'])
def support_request_collection(request):
    if request.method == 'GET':
        support_requests = SupportRequest.objects.all()
        serializer = SupportRequestSerializer(support_requests, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def client_support_request_collection(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        support_requests = SupportRequest.objects.filter(client=client)
        serializer = SupportRequestSerializer(support_requests, many=True)
        return Response(serializer.data)

# /api/support_requests/{pk}
@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def support_request_detail(request, pk):
    try:
        support_request = SupportRequest.objects.get(pk=pk)
    except SupportRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SupportRequestSerializer(support_request)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SupportRequestSerializer(support_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = SupportRequestSerializer(support_request, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        support_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
def change_support_request_status(request, pk):
    try:
        support_request = SupportRequest.objects.get(pk=pk)
    except SupportRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PATCH':
        data = {
            "status": request.data.get('status')
        }
        serializer = SupportRequestSerializer(support_request, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def make_offer(request, pk):
    try:
        support_request = SupportRequest.objects.get(pk=pk)
    except SupportRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PATCH':
        data = {
            "offer": request.data.get("offer")
        }
        serializer = SupportRequestSerializer(support_request, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def offer_response(request, pk):
    try:
        support_request = SupportRequest.objects.get(pk=pk)
    except SupportRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PATCH':
        data = {
            "response": request.data.get("response")
        }
        serializer = SupportRequestSerializer(support_request, data=data, partial=True)
        if serializer.is_valid():
            support_request.offer["response"] = data['response']
            support_request.save()
            # serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)