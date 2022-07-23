from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from incidents.models import Evaluation
from incidents.serializers import EvaluationSerializer

# /api/evaluations/
@api_view(['GET', 'POST'])
def evaluation_collection(request):
    if request.method == 'GET':
        evaluations = Evaluation.objects.all()
        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            "job": request.data.get("job"),
        }
        serializer = EvaluationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /api/evaluations/{pk}
@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def evaluation_detail(request, pk):
    try:
        evaluation = Evaluation.objects.get(pk=pk)
    except Evaluation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EvaluationSerializer(evaluation)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EvaluationSerializer(evaluation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = EvaluationSerializer(evaluation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        evaluation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
def do_test(request, pk):
    try:
        evaluation = Evaluation.objects.get(pk=pk)
    except Evaluation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PATCH':
        data = {
            "test": request.data.get("test")
        }
        serializer = EvaluationSerializer(evaluation, data=data, partial=True)
        if serializer.is_valid():
            evaluation.tests.append(data['test'])
            evaluation.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_test_results(request, pk):
    try:
        evaluation = Evaluation.objects.get(pk=pk)
    except Evaluation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PATCH':
        data = {
            "results": request.data.get("results")
        }
        serializer = EvaluationSerializer(evaluation, data=data, partial=True)
        if serializer.is_valid():
            for test in evaluation.tests:
                if test['label'] == "Boot Computer":
                    test['results'] = data['results']
                    evaluation.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)