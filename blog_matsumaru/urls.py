from django.contrib import admin
from django.urls import path
from . import views


app_name = 'blog_matsumaru'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
]
