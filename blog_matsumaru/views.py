from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import InquiryForm


class IndexView(TemplateView):
  template_name = 'blog_matsumaru/index.html'

class InquiryView(FormView):
  template_name = 'blog_matsumaru/inquiry.html'
  form_class    = InquiryForm