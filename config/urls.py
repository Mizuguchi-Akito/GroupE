from django.contrib import admin
from django.urls import path,include
from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog_matsumaru/',include('blog_matsumaru.urls')),
    path('accounts/', include('allauth.urls')),
]


#開発サーバーでメディアを配信できるようにする設定
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)