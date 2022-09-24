from django.urls import path
from .views import index,login,example

urlpatterns = [
    # path('', index, name='index'),
    path('login-ex/', login),
    path('ex/', example),

]
