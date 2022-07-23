from django.urls import path

from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home,  name='home'),
    path('<str:room_name>/', room, name='room'),
    path('checkview', checkview, name='checkview'),
    path('send', send, name='send'),
    path('<getMessages/str:room_name>/', getMessages , name='getMessages'),

              ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)