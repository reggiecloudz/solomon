from django.urls import include, path

from incidents.views import solution_collection, solution_detail, select_solution

urlpatterns = [
    path('api/solutions/', include(([
        path('', solution_collection, name='solution_collection'),
        path('<int:pk>/', solution_detail, name='solution_detail'),
        path('<int:pk>/select-solution/', select_solution, name='select_solution'),
    ], 'solution'))),
]
