from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('<int:month>', monthly_challenge_by_number),
    path('<str:month>', monthy_challenge, name="month_challenge")
]
