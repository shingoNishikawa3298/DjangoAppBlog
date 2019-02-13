from django.db import models

# Create your models here.
class Blog(models.Model):
    # id = 1,2,3,4,...が自動的に付与される
    content = models.CharField(max_length=140)
    posted_date = models.DateField(auto_now_add=True)