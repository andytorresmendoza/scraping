from django.urls import path
from .views import getcomercio

urlpatterns=[
    path('getcomercio', getcomercio,name='getcomercio'),
]