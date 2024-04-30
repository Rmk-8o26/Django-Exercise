'''from django.contrib import admin
from django.urls import path
from django.conf.urls import include

import application2
app_name=application2
urlpatterns=[
    path('admin/',admin.site.urls),
    path('app2_url/',include('application2.api_urls'))
]'''
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

import application2

app_name = 'application2'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', include('application2.api_urls'))
]
