
from django.urls import path
from .views import resume, mypage,myresume
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('resume/', resume, name='resume'),
    path('mypage/', mypage, name='mypage'),
    path('myresume', myresume,name='myresume'),

]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )