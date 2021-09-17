from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "blog_kamimura/index.html"