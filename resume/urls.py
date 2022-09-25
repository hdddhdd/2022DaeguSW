
from django.urls import path
from .views import resume, mypage,myresume,ResumeDetail,ResumeCreate,ResumeUpdate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('resume/', resume, name='resume'), # 이력서 작성하기
    path('mypage/', mypage, name='mypage'), # 마이페이지
    path('myresume', myresume,name='myresume'), # 작성한 이력서 전부 보기
    path('myresume/<int:pk>', ResumeDetail.as_view()), # 작성한 이력서 중 하나 보기
    # path('detail/<int:pk>/',resume_detail, name='resume_detail'),

    # 이력서 생성 및 수정
    path('create/', ResumeCreate.as_view()), # 이력서 생성
    path('myresume/update/<int:pk>/', ResumeUpdate.as_view()), # 이력서 수정
    path('myresume/update/2/2/', myresume), # 이력서 수정

]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )