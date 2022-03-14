from django.http import HttpResponseRedirect
from django.shortcuts import reverse

def redirect(request):
    return HttpResponseRedirect(reverse('ytdownload:download_video'))
