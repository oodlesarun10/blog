from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,default='')
    phone=models.CharField(max_length=13,default='')
    email=models.CharField(max_length=255,default='')
    content=models.TextField()
    timestamp =models.DateField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name
