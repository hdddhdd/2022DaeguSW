from django.shortcuts import render
from .models import BoardData

# Create your views here.
def job_list(request):
    job_data = BoardData.objects
    return render(request, 'crawled_job/job_list.html', {'boarddata': job_data})

def job_detail(request, pk):
    job_data = BoardData.objects.get(pk=pk)
    return render(request, 'crawled_job/job_detail.html', {'boarddata': job_data})