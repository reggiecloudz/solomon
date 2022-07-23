from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from incidents.models import Solution
from incidents.serializers import SolutionSerializer

# /api/solutions/
@api_view(['GET', 'POST'])
def solution_collection(request):
    if request.method == 'GET':
        solutions = Solution.objects.all()
        serializer = SolutionSerializer(solutions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            "label": request.data.get("label"),
            "description": request.data.get("description"),
            "overall_cost": request.data.get("overall_cost"),
            "job": request.data.get("job"),
        }
        serializer = SolutionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /api/solutions/{pk}
@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def solution_detail(request, pk):
    try:
        solution = Solution.objects.get(pk=pk)
    except Solution.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SolutionSerializer(solution)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SolutionSerializer(solution, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = SolutionSerializer(solution, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        solution.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
def select_solution(request, pk):
    try:
        solution = Solution.objects.get(pk=pk)
    except Solution.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PATCH':
        data = {
            "is_selected": request.data.get("is_selected")
        }
        serializer = SolutionSerializer(solution, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
