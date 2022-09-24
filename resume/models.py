from django.db import models

from django.contrib.auth.models import User

# from phonenumber_field.formfields import PhoneNumberField
# Create your models here.

class Resume(models.Model):
    user_img = models.FileField(upload_to='Uploaded Files/')
    user_phonenum = models.CharField(max_length=20, verbose_name='전화번호')
    user_name = models.CharField(max_length=30,  verbose_name='이름')
    user_gender = models.CharField(max_length=100, verbose_name='성별')
    user_address = models.TextField(max_length=100, verbose_name='주소')
    user_disability = models.CharField(max_length=100, verbose_name='장애')
    # phone_num = PhoneNumberField()


    #경력 및 경험을 콤보박스로 나타내고 싶다.
    user_career = models.TextField(max_length=500, verbose_name='경력 및 경험')

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return f'{self.pk}/'
