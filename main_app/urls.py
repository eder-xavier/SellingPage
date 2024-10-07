from django.urls import path 
from django.contrib import admin
from . import views

app_name = 'main_app'

urlpatterns = [

    path('', views.home,  name='home'),

]