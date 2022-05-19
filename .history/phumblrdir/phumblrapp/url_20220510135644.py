from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('phumblrapp.urls')),
    path('accounts/', include('django.contrib.auth')),
]
