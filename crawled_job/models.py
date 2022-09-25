from django.db import models
from django.urls import reverse

# Create your models here.
class BoardData(models.Model):
    field = models.IntegerField(default=0)
    link = models.URLField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    salary_type = models.CharField(max_length=30)
    salary = models.CharField(max_length=30)
    regular = models.CharField(max_length=20)
    detail = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_company(self):
        return self.company

    def get_absolute_url(self):
        return reverse('crawled_job:job_detail', kwargs={'pk':self.id} )
    
    class Meta:
        db_table = 'board_data'