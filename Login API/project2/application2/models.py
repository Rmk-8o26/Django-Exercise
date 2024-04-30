from django.db import models

#create your models here
class login_model(models.Model):
    username=models.EmailField(max_length=70,blank=False,null=False)
    password=models.CharField(max_length=70,blank=False,null=False)
    is_active=models.BooleanField(default=True) 