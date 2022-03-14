import io
from django.http import (
    HttpResponse,
    StreamingHttpResponse
    )
from django.shortcuts import render

from pytube import YouTube

from .forms import DownloadYoutubeForm


def download_video(request):
    if request.method == 'POST' and 'video' in request.POST:
        form = DownloadYoutubeForm(request.POST)
        if form.is_valid():
            video_link = form.cleaned_data['video_link']
            with io.BytesIO() as file_buffer:
                YouTube(video_link).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').last().stream_to_buffer(file_buffer)
                # YouTube(video_link).streams.get_audio_only().stream_to_buffer(file_buffer)
                response = HttpResponse(file_buffer.getvalue(), content_type='video/mp4')
                # response = HttpResponse(file_buffer.getvalue(), content_type='audio/mp3')
                response['Content-Disposition'] = 'attachment; filename=video.mp4'
                return response
    elif request.method == 'POST' and 'audio' in request.POST:
        form = DownloadYoutubeForm(request.POST)
        if form.is_valid():
            video_link = form.cleaned_data['video_link']
            with io.BytesIO() as file_buffer:
                YouTube(video_link).streams.get_audio_only().stream_to_buffer(file_buffer)
                response = HttpResponse(file_buffer.getvalue(), content_type='audio/mp3')
                response['Content-Disposition'] = 'attachment; filename=audio.mp3'
                return response
    else:
            form = DownloadYoutubeForm()

    return render(request, 'download_youtube.html', {'form': form})




