from django.db import models

#create your models here
class savings_model(models.Model):
    name=models.CharField(max_length=70,blank=False,null=False)
    age=models.IntegerField(blank=False,null=False)
    amount=models.IntegerField(blank=False,null=False)
    is_active=models.BooleanField(default=True) 