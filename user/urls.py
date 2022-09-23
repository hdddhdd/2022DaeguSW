
from django.urls import path
from .views import signup,result


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('result/', result, name='result'),
]