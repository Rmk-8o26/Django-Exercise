from .views import login_api
from django.urls import path,include
import application2
app_name='application2'
urlpatterns=[
    
    path('savings_url/',login_api.as_view())
]


"""path('app2_url/',include('project2.urls')),
    path('api-auth/',include('rest_framework.urls')),"""