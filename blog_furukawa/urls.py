"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .import views

app_name = 'blog_furukawa'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('blog-list/', views.BlogListView.as_view(), name="blog_list"),
    path('blog-detail/<int:pk>/', views.BlogDetailView.as_view(), name="blog_detail"),
    path('blog-create/', views.BlogCreateView.as_view(), name="blog_create"),
    path('blog-update/<int:pk>/', views.BlogUpdateView.as_view(), name="blog_update"),
    path('blog-delete/<int:pk>/', views.BlogDeleteView.as_view(), name="blog_delete"),
]
