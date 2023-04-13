from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:artilce_pk>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('delete/<int:artilce_pk>/', views.delete, name='delete'),
]
