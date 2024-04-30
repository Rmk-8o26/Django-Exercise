from .views import Medicine_api
from django.urls import path,include
import app
app_name='app'
urlpatterns=[
    
    path('medicine_url/',Medicine_api.as_view()),
]