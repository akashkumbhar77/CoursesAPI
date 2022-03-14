from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getallData),
    path('getCourse/<str:pk>',views.getCourseInfo),
    path('getallProducts',views.getallProducts),
    path('getProduct/<str:pk>',views.getProduct)
]