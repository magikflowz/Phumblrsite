from django.contrib import admin
from 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('phumblrapp.urls')),
    path('accounts/', include('django.contrib.auth')),
]
