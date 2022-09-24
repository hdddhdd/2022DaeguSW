
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from resume.models import Resume

# resume 등록 및 수정
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView
from django.core.exceptions import PermissionDenied
# from django.contrib.auth.mixins import LoginRequiredMixin
from . import models

from django.shortcuts import get_object_or_404


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
        #resume.save()

        return HttpResponseRedirect('/')

    return render(request, 'main.html')

        
def myresume(request):
    resumes = Resume.objects.all()
    context = {'resumes':resumes}
    return render(request, 'myresume.html', context)

def resume_detail(request,pk):
    login_session = request.session.get('login_session','')
    context = {'login_session':login_session}
    resume = get_object_or_404(Resume, id=pk)
    context['resume'] = resume

    return render(request, 'resume_detail.html', context)

class ResumeDetail(DetailView):
    model = Resume

# 이력서 작성하기
class ResumeCreate(LoginRequiredMixin, CreateView):
    model = Resume
    fields = ['user_img', 'user_phonenum', 'user_name', 'user_gender', 'user_address', 'user_disability', 'user_career']
    template_name = 'resume/resume_form.html'

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(ResumeCreate, self).form_valid(form)
        else:
            return redirect('/resume/')



# 이력서 수정하기
class ResumeUpdate(LoginRequiredMixin, UpdateView):
    model = Resume
    fields = ['user_img', 'user_phonenum', 'user_name', 'user_gender', 'user_address', 'user_disability', 'user_career']

    template_name = 'resume/resume_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(ResumeUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied




