from django.contrib import admin
from . import view

urlpatterns = [
    path('', views.index, name='indx'),
    path('', include('phumblrapp.urls')),
    path('accounts/', include('django.contrib.auth')),
]
