from django import forms
from django.core.validators import URLValidator

from pytube import YouTube

class DownloadYoutubeForm(forms.Form):
    video_link = forms.CharField(max_length=200, label=False, validators=[URLValidator()])

    def clean_video_link(self):
        data = self.cleaned_data.get('video_link')

        try:
            YouTube(data)
            return data
        except Exception as e:
            raise forms.ValidationError(e)

