from django.contrib import admin
from .models import RepM
# Register your models here.

@admin.register(RepM)
class RepM_a(admin.ModelAdmin):
    list_display=['sno','drug_name','drug_strength','drug_type','bill_date']
