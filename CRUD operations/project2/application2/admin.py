from django.contrib import admin
from .models import savings_model
#register your models here
@admin.register(savings_model)
class savings_models_a(admin.ModelAdmin):
    list_display=['id','name','age','amount']