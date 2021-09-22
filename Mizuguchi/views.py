from django.shortcuts import render
from django.views import generic
# Create your views here.
class MizuguchiView(generic.TemplateView):
    template_name = "Mizuguchi/index.html"