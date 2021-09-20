from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages 
from .forms import InquiryForm


class IndexView(TemplateView):
  template_name = 'blog_matsumaru/index.html'

class InquiryView(FormView):
  template_name = 'blog_matsumaru/inquiry.html'
  form_class    = InquiryForm
  success_url   = reverse_lazy('blog_matsumaru:inquiry')

  def form_valid(self, form):
    form.send_email()
    messages.success(self.request, 'メッセージを送信しました。')
    return super().form_valid(form)