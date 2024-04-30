from .views import savings_api
from django.urls import path,include
import application2
app_name='application2'
urlpatterns=[
    
    path('savings_url/',savings_api.as_view())
]


"""path('app2_url/',include('project2.urls')),
    path('api-auth/',include('rest_framework.urls')),"""