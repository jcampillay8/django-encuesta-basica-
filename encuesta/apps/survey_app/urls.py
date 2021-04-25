from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.create_survey),
    path('result', views.result),
    path('go_back', views.back)
]