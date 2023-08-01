from django.urls import path
from app12.views import *
app_name='app12'


urlpatterns = [
    path('prime/',prime,name='prime'),
]