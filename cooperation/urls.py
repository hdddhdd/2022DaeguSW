from django.urls import path
from . import views

app_name = 'cooperation'
urlpatterns = [
    path('', views.PostList.as_view()),
    path('<str:slug>/', views.trainingList_page),
    path('<str:slug>/<int:pk>/', views.PostDetail.as_view()),
    path('<str:q>/', views.CompanySearch.as_view()),
]