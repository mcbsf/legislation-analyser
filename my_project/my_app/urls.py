
from django.contrib import admin
from django.urls import path
from my_app import views as my_app_views

urlpatterns = [
    path('', my_app_views.index),
    path('analyse_files', my_app_views.analyse_files, name='analyse_files'),
]
