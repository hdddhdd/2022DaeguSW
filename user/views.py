from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import HttpResponseRedirect

from user.models import User

def result(request):
    return render(request, 'result.html')


def signup(request):
    if request.method == 'GET':
        return render (request, 'signup.html')

    elif request.method == 'POST':
        user_id = request.POST.get('id')
        user_pw = request.POST.get('password')
        user_name = request.POST.get('username')
        user_gender = request.POST.get('gender')
        user_disability = request.POST.get('disability')
        user_phonenum = request.POST.get('phonenum')
        user_interest = request.POST.get('interest')

        if (user_id or user_pw or user_pw or user_name or user_gender
        or user_disability or user_phonenum or user_interest) == '':
            return redirect('login.html')
        else:
            user = User(
                user_id = user_id,
                user_pw = user_pw,
                user_name=user_name,
                user_gender=user_gender,
                user_disability=user_disability,
                user_phonenum=user_phonenum,
                user_interest=user_interest,
            )
            user.save()
            return HttpResponseRedirect('/')
    return render(request, 'login.html')

        
    