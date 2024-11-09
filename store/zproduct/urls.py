from django.urls import path
from .views import welcomePage, signin, login, activate
from .endpoints import setData, createVerification

urlpatterns = [
    path('', welcomePage),
    path('sign', signin),
    path('log', login),
    path('activation', activate),
    #ENDPOINTS
    path('setData', setData),
    path('verf', createVerification),
]