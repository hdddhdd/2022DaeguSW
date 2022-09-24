from django.contrib import admin
from .models import Post, PostLocationCategory, CompanyName, Training, TrainingCategory

admin.site.register(Post)
admin.site.register(Training)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(CompanyName, CategoryAdmin)
admin.site.register(PostLocationCategory, CategoryAdmin)
admin.site.register(TrainingCategory, CategoryAdmin)
