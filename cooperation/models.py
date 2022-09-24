from django.db import models
import os

# 연계 기관 클래스 

# 연계 기관 이름 - 기관별로 직업훈련 목록을 따로 보여줘야하기 때문에 이름을 카테고리화함
class CompanyName(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(null=False, max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Name of Companies'

    def get_absolute_url(self):
        return f'/cooperation/{self.slug}/'
    

# 연계 기관 위치 - 지역별로 기관을 볼 때 사용하기 위해 카테고리화함
class PostLocationCategory(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(null=True, max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'LocationCategories'


# 연계 기관
class Post(models.Model):

    companyImage = models.ImageField(upload_to='cooperation/images/%Y/%m/%d/', blank=True) # 기업 대표 이미지
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='post_CompanyName') # 기업 이름

    companyHook = models.CharField(max_length = 100, blank = True) # 기업 짧은 소개
    companyLocationCategory = models.ForeignKey(PostLocationCategory, null=True, blank=True, on_delete=models.SET_NULL) # 기업 위치

    companyNumber = models.CharField(max_length=13, blank=True) # 기업 전화번호
    companyInform = models.CharField(max_length = 50) # 기업 소개
    companyDomain = models.URLField() # 기업 도메인 주소

    def __str__(self):  # 기업 이름, pk 보여주기
        return f'[{self.pk}]{self.companyName}'

    def get_absolute_url(self):
        return f'/cooperation/{self.companyName}/'



# 기관 직업훈련 클래스
class TrainingCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(null=True, max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'TrainingCategories'


class Training(models.Model):
    trainingImage = models.ImageField(upload_to='cooperation/images/training/%Y/%m/%d/', blank=True) # 직업 훈련 썸네일
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='training_CompanyName') # 기업 이름
    
    trainingTitle = models.CharField(max_length = 50) # 직업 훈련 이름
    trainingType = models.CharField(max_length = 30) # 직업 훈련 유형
    trainingCategory = models.ForeignKey(TrainingCategory, null=True, blank=True, on_delete=models.SET_NULL) # 직업 훈련 타입 (대면 / 비대면 / 혼합)

    trainingContents = models.TextField() # 직업 훈련 내용
    trainingFile = models.FileField(upload_to='cooperation/files/training/%Y/%m/%d/', blank=True) # 직업 훈련 관련 파일

    def __str__(self):  # 포스트 제목과 번호 보여주기
        return f'[{self.pk}]{self.trainingTitle}'

    def get_absolute_url(self):
        return f'/cooperation/{self.companyName}/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
