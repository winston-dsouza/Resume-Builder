from django.urls import path
from . import views


urlpatterns = [
    path('', views.resume , name='resume'),

]
