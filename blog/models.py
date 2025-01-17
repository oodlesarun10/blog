from django.db import models

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255,default='')
    author=models.CharField(max_length=255,default='')
    content=models.TextField(max_length=10000)
    slug=models.CharField(max_length=255,default='')
    timestamp =models.DateField(blank=True)

    def __str__(self):
        return self.title + "by" + self.author
