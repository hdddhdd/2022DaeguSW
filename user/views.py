from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_http_methods
from user.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404

# @require_http_methods(["GET", "POST"])
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)

#         if form.is_valid():
#             user_id = form.cleaned_data.get("id")
#             user_pw = form.cleaned_data.get("password")
#             user = authenticate(request=request, user_id =user_id, user_pw=user_pw)

#             if user is not None:
#                 login(request,user)
#             return redirect("home")
#         else:
#             return redirect("home")
#     else:
#         form = AuthenticationForm()
#         return render(request, 'login.html', {'form':form})
def login_view(request):
    if request.method=="GET":
        return render (request, 'login.html')
    elif request.method == "POST" :
        #전송받은 이메일 비밀번호 확인
        user_id = request.POST.get('id')
        user_pw = request.POST.get('password')

        #유효성 처리
        res_data ={}
      
        if not (user_id and user_pw):
            res_data['error']="모든 칸을 다 입력해주세요"
        else:
            # 기존(DB)에 있는 Fuser 모델과 같은 값인 걸 가져온다.
            fuser = User.objects.get(user_id = user_id) #(필드명 = 값)

            # 비밀번호가 맞는지 확인한다. 위에 check_password를 참조
            #내가 입력한 비번과 디비에 있는 비번이 일치하는가
            if check_password(user_pw, fuser.user_pw):
                #응답 데이터 세션에 값 추가. 수신측 쿠키에 저장됨
                request.session['user']=fuser.user_id

                #리다이렉트
                return redirect('/')
            else:
                #맞는 비번도 자꾸 틀렸다 함.
                res_data['error'] = "비밀번호가 틀렸습니다."
                #여기 코드 원래 로그인 실팬데 자꾸 성공해야 하는데도 여기로 와서
                #일단 성공코드 여기에 작성

        return redirect('../main/') #응답 데이터 res_data 전달

        # return render(request,'login.html',res_data) #응답 데이터 res_data 전달


def experience(request):
    return render(request, 'experience.html')



def main(request):
    return render(request, 'main.html')


def accounts(request):
    return render(request, 'accounts.html')

def help(request):
    return render(request, 'help.html')


def logout_view(request):
    auth.logout(request)
    return redirect("home")

def result(request):
    return render(request, 'result.html')


def home(request):
    return render(request, 'home.html')

# def login(request):
#     if request.method == 'POST':
        
#         user_id = request.POST.get('id')
#         user_pw = request.POST.get('password')
        
#         user = auth.authenticate(request, user_id=user_id, user_pw=user_pw)
#         if user is not None:
#             auth.login(request, user)
#             return render(request, 'main.html')
#         else:
#             return HttpResponse('로그인 실패')
#             # return render(request, 'login.html', {'error': '아이디 또는 비밀번호가 올바르지 않습니다.'})
#     else:
#         return render(request, 'login.html')

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

        
    