from django.contrib import admin
from crawled_job.models import BoardData

class JobAdmin(admin.ModelAdmin):
    list_display= ('id', 'field', 'company', 'title',)

admin.site.register(BoardData, JobAdmin)