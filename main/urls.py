from .views import *
from django.urls import path

urlpatterns = [

    path('', create_post, name='home'),
    
    ]