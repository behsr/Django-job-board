from django.db import models

# Create your models here.

JOB_TYBE = (
    ("Full Time","Full Time"),
    ("Part Time","Part Time"),
)
class job(models.Model):
    title = models.CharField(max_length=100)
    job_tybe = models.CharField(max_length=15, choices=JOB_TYBE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experince = models.IntegerField(default=1)
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
