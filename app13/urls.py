from django.urls import path
from app13.views import *
app_name='app13'


urlpatterns = [
 
    path('even/',even,name='even'),

]