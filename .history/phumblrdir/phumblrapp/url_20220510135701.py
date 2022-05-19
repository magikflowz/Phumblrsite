from django.urls import pat
from . import views

urlpatterns = [
    path('', views.index, name='index'),
   
]
