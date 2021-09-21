from django.shortcuts import render
from django.views import generic
import logging
from django.urls import reverse_lazy 
from .models import Blog_ohno 
# from .forms import InquiryForm

logger = logging.getLogger(__name__)

from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'blog_ohno/index.html')

class IndexView(generic.TemplateView):
    template_name = "blog_ohno/index.html"

# class InquiryView(generic.FormView):
#     template_name = "blog_ohno/inquiry.html"
#     form_class = InquiryForm
#     success_url = reverse_lazy('blog_ohno:inquiry')


#     def form_valid(self, form):
#         form.send_email()
#         messages.success(self.request, 'メッセージを送信しました。')
#         logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
#         return super().form_valid(form)


from django.contrib.auth.mixins import LoginRequiredMixin


class Blog_ohnoListView(LoginRequiredMixin, generic.ListView):
    model = Blog_ohno
    template_name = 'blog_ohno_list.html'

    def get_queryset(self):
        blog_ohnos = blog_ohno.objects.filter(user=self.request.user).order_by('-created_at')
        return blog_ohnos


class Blog_ohnoListView(LoginRequiredMixin, generic.ListView):
    model = Blog_ohno
    template_name = 'blog_ohno_list.html'
    paginate_by = 2

    def get_queryset(self):
        blog_ohnos = Blog_ohno.objects.filter(user=self.request.user).order_by('-created_at')
        return blog_ohnos


class Blog_ohnoDetailView(LoginRequiredMixin, generic.DetailView):
    model = Blog_ohno
    template_name = 'blog_ohno_detail.html'
    pk_url_kwarg = 'pk'



from .forms import Blog_ohnoCreateForm

class Blog_ohnoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Blog_ohno
    template_name = 'blog_ohno_create.html'
    form_class = Blog_ohnoCreateForm 
    success_url = reverse_lazy('blog_ohno:blog_ohno_list')

    def form_valid(self,form):
        blog_ohno = form.save(commit=False)
        blog_ohno = self.request.user 
        blog_ohno.save()
        messages.success(self.request,'ブログを作成しました。')
        return super().form_valid(form)

        def form_invalid(self,form):
            messages.error(self.request,"ブログの作成に失敗しました。")
            return super().form_invalid(form)


class Blog_ohnoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Blog_ohno
    template_name = 'blog_ohno_update.html'
    form_class = Blog_ohnoCreateForm 

    def get_success_url(self):
        return reverse_lazy('blog_ohno:blog_ohno_detail',kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request,'ブログを更新しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"ブログの更新に失敗しました。")
        return super().form_invalid(form)


class Blog_ohnoDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Blog_ohno
    template_name = 'blog_ohno_delete.html'
    success_url = reverse_lazy('blog_ohno:blog_ohno_list')

    def delete(self,request, *args,**kwargs):
        messages.success(self.request, "ブログを削除します。")
        return super().delete(request,*args,**kwargs)
    