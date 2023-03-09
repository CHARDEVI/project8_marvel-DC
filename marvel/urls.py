from marvel.views import *
from django.urls import path
app_name='charishma'


urlpatterns=[
    path('captain/',captain,name='captain'),
]