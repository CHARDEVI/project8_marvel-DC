from django.urls import path
from DC.views import *

app_name='CHARISHMA'
urlpatterns=[
    path('batman/',batman,name='batman'),
]