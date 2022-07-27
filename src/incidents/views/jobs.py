from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from incidents.models import Job, ServiceOrder
from incidents.serializers import JobSerializer

# /api/jobs/
@api_view(['GET', 'POST'])
def sevice_order_job_collect(request, pk):
    try:
        service_order = ServiceOrder.objects.get(pk=pk)
    except ServiceOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        job = Job.objects.get(service_order=service_order)
        serializer = JobSerializer(job, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            "label": request.data.get("label"),
            "priority": "Normal",
            "service_order": service_order.pk,
            "technician": service_order.technician.pk,
        }
        serializer = JobSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /api/jobs/
@api_view(['GET'])
def job_collection(request):
    if request.method == 'GET':
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# /api/jobs/{pk}
@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def job_detail(request, pk):
    try:
        job = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JobSerializer(job)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = JobSerializer(job, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)