from django.urls import path

from . import views


app_name = 'mizuguchi'

urlpatterns = [
    path('',views.MizuguchiView.as_view(), name="index"),
]