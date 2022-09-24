from django.contrib import admin
from .models import User

@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'user_pw',
        'user_name',
        'user_gender',
        'user_disability',
        'user_phonenum',
        'user_interest',
    )

  