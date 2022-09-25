from django.urls import path
from . import views
import crawled_job.views

app_name = 'crawled_job'
urlpatterns = [
    
    path('', views.job_list, name='job_list'),
    #path('job_detail/', crawled_job.views.job_detail, name='job_detail')
    path('job_detail/<int:pk>/', crawled_job.views.job_detail, name = 'job_detail')
]
