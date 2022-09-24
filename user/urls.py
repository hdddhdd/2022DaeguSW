
from xml.etree.ElementInclude import include
from django.urls import path
from .views import signup,result, login_view,logout_view,home, main, help, accounts,mypage

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('result/', result, name='result'),
    #path('login/', login, name='login'),
    path('login/', login_view, name="login_view"),
    path('logout/', logout_view, name="logout_view"),
    path('home/', home, name='home'),
    path('', main, name='main'),
    path('help/', help, name='help'),
    path('yey/', accounts, name='accounts'),
    path('mypage/', mypage, name='mypage'),
]