import logging
from django.urls import reverse_lazy

from django.views import generic

from .forms import ContactForm

from django.contrib import messages

logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "blog_kamimura/index.html"

class ContactView(generic.FormView):
    template_name = "blog_kamimura/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('blog_kamimura:contact')

    def form_valid(self, form):
      form.send_email()
      messages.success(self.request,'メッセージを送信しました。')
      logger.info('Contact sent by {}'.format(form.cleaned_data['name']))
      return super().form_valid(form)