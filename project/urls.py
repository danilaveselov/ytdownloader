from django.contrib import admin
from django.urls import path, include

from .views import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=redirect),
    path('', include('ytdownload.urls', namespace='ytdownload')),
]
