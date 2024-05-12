
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('protect/', include('protect.urls')),
    #path('', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('Board_News.urls')),
]
