from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from incidents.models import Implementation
from incidents.serializers import ImplementationSerializer

# /api/implementations/
@api_view(['GET', 'POST'])
def implementation_collection(request):
    if request.method == 'GET':
        implementations = Implementation.objects.all()
        serializer = ImplementationSerializer(implementations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            "plan": request.data.get("plan"),
            "solution": request.data.get("solution"),
        }
        serializer = ImplementationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /api/implementations/{pk}
@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def implementation_detail(request, pk):
    try:
        implementation = Implementation.objects.get(pk=pk)
    except Implementation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ImplementationSerializer(implementation)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ImplementationSerializer(implementation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = ImplementationSerializer(implementation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        implementation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
