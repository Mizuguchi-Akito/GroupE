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
from . import views

app_name = 'blog_ohno'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog_list/',views.Blog_ohnoListView.as_view(),name="blog_ohno_list"),
    path('blog_detail/<int:pk>/', views.Blog_ohnoDetailView.as_view(),name="blog_ohno_detail"),
    path('blog_create/',views.Blog_ohnoCreateView.as_view(),name="blog_ohno_create"),
    path('blog_update/<int:pk>/',views.Blog_ohnoUpdateView.as_view(),name="blog_ohno_update"),
    path('blog_delete/<int:pk>/',views.Blog_ohnoDeleteView.as_view(),name="blog_ohno_delete"),
]
