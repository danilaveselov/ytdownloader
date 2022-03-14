from django.apps import apps
from django.urls import path

from .views import download_video

app_name = apps.get_app_config('ytdownload').name

urlpatterns = [
    path('ytdownloader/download/', download_video, name='download_video'),
]
