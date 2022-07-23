from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from incidents.models import ProblemDefinition
from incidents.serializers import ProblemDefinitionSerializer

# /api/problem_definitions/
@api_view(['GET', 'POST'])
def problem_definition_collection(request):
    if request.method == 'GET':
        problem_definitions = ProblemDefinition.objects.all()
        serializer = ProblemDefinitionSerializer(problem_definitions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            "context": request.data.get("context"),
            "background": request.data.get("background"),
            "symptoms": request.data.get("symptoms"),
            "job": request.data.get("job"),
        }
        serializer = ProblemDefinitionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /api/problem_definitions/{pk}
@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def problem_definition_detail(request, pk):
    try:
        problem_definition = ProblemDefinition.objects.get(pk=pk)
    except ProblemDefinition.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProblemDefinitionSerializer(problem_definition)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProblemDefinitionSerializer(problem_definition, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = ProblemDefinitionSerializer(problem_definition, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        problem_definition.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
