from django.contrib import admin
from django.urls import path,include

app_name=['apps']

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.urls')),
]
