from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from resume.models import Resume
from . import models

def mypage(request):
    return render(request, 'mypage.html')

def resume(request):
    if request.method == 'GET':
        return render (request, 'resume.html')

    elif request.method == 'POST':
        #user_id = request.POST.get('id')
        user_img = request.FILES.get('user_img')
        user_name = request.POST.get('user_name')
        user_phonenum = request.POST.get('user_phonenum')
        user_gender = request.POST.get('user_gender')
        user_address = request.POST.get('user_address')
        user_disability = request.POST.get('disability')
        user_career = request.POST.get('user_career')

       
        resume = Resume(
            user_img = user_img,
            user_name=user_name,
            user_phonenum=user_phonenum,
            user_gender=user_gender,
            user_address=user_address,
            user_disability=user_disability,
            user_career=user_career,
        )
        resume.save()

        return HttpResponseRedirect('/')

    return render(request, 'main.html')

        
def myresume(request):
    
    resumes = Resume.objects.all()
    context = {'resumes':resumes}
    return render(request, 'myresume.html', context)