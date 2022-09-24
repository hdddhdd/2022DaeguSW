from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns=[

    path('blog/', views.index),
    path('create_post/', views.PostCreate.as_view()),
]