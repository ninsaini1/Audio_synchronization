from django.conf.urls import url
from django.urls import path

from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('sync', views.sync, name='sync'),
    path('about',views.about, name='about'),
    path('result',views.result, name='result'),
    path('home',views.index, name='home')
    ]

urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)