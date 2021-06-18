from django.shortcuts import render
from django.http import HttpResponse

from . import models
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def sync(request):
    if request.method == 'POST':          
        title = request.POST['title1']
        video = request.POST['audio1']
         
        content = models.Videos(title=title,video=video)
        content.save()

        title2 = request.POST['title2']
        video2 = request.POST['audio2']

        content2 = models.Videos(title=title2, video=video2)
        content2.save()
        return redirect('index')
     
    return render(request, 'result.html')
