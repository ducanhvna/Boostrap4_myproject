from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='main-view'),
    path('add', views.PersonCreateView.as_view(), name='person-add')
]