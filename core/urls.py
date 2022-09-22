from django.urls import path
from .views import index,login,example

urlpatterns = [
    path('', index, name='index'),
    path('login/', login),
    path('ex/', example),

]
