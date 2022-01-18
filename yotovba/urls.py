from django.urls import path
from .views import *

app_name = 'yotovba'

urlpatterns = [
    path('', index, name='home'),
    path('download/', download, name='download'),
    path('download/<resolution>', donwload_done, name='download_done'),
]
