from django.urls import include, path

from .views import logout_view, ClientSignUpView

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', ClientSignUpView.as_view(), name='client_signup'),
]