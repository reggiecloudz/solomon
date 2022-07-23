from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from incidents.models import RootCause
from incidents.serializers import RootCauseSerializer

# /api/root_causes/
@api_view(['GET', 'POST'])
def root_cause_collection(request):
    if request.method == 'GET':
        root_causes = RootCause.objects.all()
        serializer = RootCauseSerializer(root_causes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            "cause": request.data.get("cause"),
            "findings": request.data.get("findings"),
            "job": request.data.get("job"),
        }
        serializer = RootCauseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /api/root_causes/{pk}
@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def root_cause_detail(request, pk):
    try:
        root_cause = RootCause.objects.get(pk=pk)
    except RootCause.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RootCauseSerializer(root_cause)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RootCauseSerializer(root_cause, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = RootCauseSerializer(root_cause, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        root_cause.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)