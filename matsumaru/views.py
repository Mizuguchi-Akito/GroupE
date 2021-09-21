from re import template
from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
  template_name = 'matsumaru/index.html'

