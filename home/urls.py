from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.iintroduction,name='home'),
    #path('c/',views.cve,name='c'),
    #path()
    #path('cart/',views.cartt,name='cart')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
