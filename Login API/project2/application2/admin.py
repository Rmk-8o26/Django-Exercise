from django.contrib import admin
from .models import login_model
#register your models here
@admin.register(login_model)
class login_models_a(admin.ModelAdmin):
    list_display=['username','password']