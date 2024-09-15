from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('regi/',regi,name="regi"),
    path('login/',login,name="login"),
    path('delete/',delete,name="delete")
]
