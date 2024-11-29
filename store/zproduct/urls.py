from django.urls import path
from .views import welcomePage, signin, login, activate, profile
from .endpoints import setData, createVerification
from rest_framework_simplejwt import views

urlpatterns = [
    #Views
    path('', welcomePage),
    path('sign', signin),
    path('log', login),
    path('activation', activate),
    path('profile', profile),
    #ENDPOINTS
    path('setData', setData),
    path('verf', createVerification),
    #AUTH
    path('api/token/', views.TokenObtainPairView.as_view(), name='default'),
    path('api/token/refresh/', views.TokenRefreshView.as_view(), name='refresh'),
    path('api/token/verify/', views.TokenVerifyView.as_view(), name='verify'),
]