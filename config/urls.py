from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ohno/',include('ohno.urls')),
    path('matsumaru/',include('blog_matsumaru.urls')),
    path('furukawa/',include('furukawa.urls')),
    path('mizuguchi', include('Mizuguchi.urls')),
    path('kamimura', include('Kamimura.urls')),
    path('accounts/', include('allauth.urls')),

]
