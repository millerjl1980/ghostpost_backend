from django.urls import path
from ghostpost import views

urlpatterns = [
    path('addpost', views.addpost),
]