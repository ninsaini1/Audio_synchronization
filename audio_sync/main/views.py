from django.shortcuts import render
from django.http import HttpResponse

from . import models
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def result(request):
    return render(request, 'result.html')

def sync(request):
    if request.method == 'POST':          
        title1 = request.POST['title1']
        video1 = request.POST['audio1']
         
        content = models.Videos(title=title1,video=video1)
        content.save()

        title2 = request.POST['title2']
        video2 = request.POST['audio2']

        content2 = models.Videos(title=title2, video=video2)
        content2.save()

        title3 = request.POST['title3']
        video3 = request.POST['audio3']

        
        content3 = models.Videos(title=title3, video=video3)
        content3.save()
        # return redirect('index')
     
    return render(request, 'result.html')
