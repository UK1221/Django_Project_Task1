from django.contrib import admin
from django.urls import path
from  .views import *


urlpatterns = [
    path("",createpost,name='createpost'),
    path('viewpost/', viewpost, name='viewpost'),
    path('deleteProfile/<int:pk>/', delet, name='deleteProfile'),
    path('updateUserProfile/<int:pk>/',
         update, name='updateUserProfile'),
]
