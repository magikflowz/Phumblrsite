from django.contrib import admin
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('phumblrapp.urls')),
    path('accounts/', include('django.contrib.auth')),
]
