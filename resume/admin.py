from django.contrib import admin
from .models import Resume

@admin.register(Resume)

class ResumeAdmin(admin.ModelAdmin):
    list_display = (
       
        'user_img',
        'user_name',
        'user_phonenum',
        'user_gender',
        'user_disability',
        'user_career',
    )
