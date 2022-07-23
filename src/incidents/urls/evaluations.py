from django.urls import include, path

from incidents.views import evaluation_collection, evaluation_detail, do_test, update_test_results

urlpatterns = [
    path('api/evaluations/', include(([
        path('', evaluation_collection, name='evaluation_collection'),
        path('<int:pk>/', evaluation_detail, name='evaluation_detail'),
        path('<int:pk>/test/', do_test, name='do_test'),
        path('<int:pk>/update-results/', update_test_results, name='update_test_results'),
    ], 'evaluation'))),
]
