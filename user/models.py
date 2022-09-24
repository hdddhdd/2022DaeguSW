from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=30, unique=True, verbose_name='아이디')
    user_pw = models.CharField(max_length=50, verbose_name='비밀번호')
    user_name = models.CharField(max_length=30, unique=True, verbose_name='이름')
    user_gender = models.CharField(max_length=10, verbose_name='성별')
    user_disability = models.CharField(max_length=10, verbose_name='장애')
    user_phonenum = models.CharField(max_length=20, verbose_name='전화번호')
    user_interest = models.CharField(max_length=30, verbose_name='관심분야')

def __str__(self):
    return self.user_id

