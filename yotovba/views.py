from django.shortcuts import render
from pytube import YouTube
import os


def index(request):
    return render(request, 'main.html')


def download(request):
    global url
    url = request.GET.get('url')
    yt = YouTube(url)
    strm_all = []
    strm_all = yt.streams.filter(progressive=True).all()
    embed_link = url.replace("watch?v=", "embed/")
    title = yt.title
    context = {
        'video': strm_all,
        'embed_link': embed_link,
        'title': title,
    }
    return render(request, 'download.html', context)


def donwload_done(request, resolution):
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    if request.method == 'POST':
        vidyo = YouTube(url)
        video = vidyo.streams.filter(res=resolution).first()
        video.download(dirs)
        # YouTube(url).streams.get_by_resolution(resolution).download()
        return render(request, 'done.html')
    else:
        return render(request, 'error.html')
