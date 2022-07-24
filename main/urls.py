
from django.contrib import admin
from django.urls import path,include
from . import views 
urlpatterns = [
    path('test',views.test,name="test"),
    path('',views.get_data,name="get_data"),
    path('load',views.load_app_name,name="load_app_name")
]
