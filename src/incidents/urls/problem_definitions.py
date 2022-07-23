from django.urls import include, path

from incidents.views import problem_definition_collection, problem_definition_detail

urlpatterns = [
    path('api/problem-definitions/', include(([
        path('', problem_definition_collection, name='problem_definition_collection'),
        path('<int:pk>/', problem_definition_detail, name='problem_definition_detail'),
    ], 'problem_definition'))),
]
