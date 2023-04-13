from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:artilce_pk>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('delete/<int:artilce_pk>/', views.delete, name='delete'),
    path('update/<int:article_pk>/', views.update, name='update'),
    path('detail/<int:article_pk>/comments/', views.comment_create, name='comment_create'),
    path('detail/<int:article_pk>/comments/delete/<int:comment_pk>/', views.comment_delete, name='comment_delete'),    
]
