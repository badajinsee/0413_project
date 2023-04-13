from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:review_pk>', views.detail, name='detail'),
]
