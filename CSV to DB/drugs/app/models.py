from django.db import models

# Create your models here.
class RepM(models.Model):
    sno=models.IntegerField(blank=False,null=False)
    drug_name=models.CharField(max_length=20,blank=False,null=False)
    drug_strength=models.CharField(max_length=20,blank=False,null=False)
    drug_type=models.CharField(max_length=10,blank=False,null=False)
    bill_date=models.DateField(blank=False,null=False)
    is_active=models.BooleanField(default=True)
