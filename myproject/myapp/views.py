from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Blog
from .models import notice
from .models import communicate
# Create your views here.

def layout(request):
    return render(request,'myapp/layout.html')

def layout2(request):
    communicates = communicate.objects
    return render(request,'myapp/layout2.html', {'communicates':communicates})

def layout3(request):
    notices = notice.objects
    return render(request,'myapp/layout3.html', {'notices':notices})

def layout4(request):
    blogs = Blog.objects
    return render(request,'myapp/layout4.html', {'blogs':blogs})

def create(request):
    communicates = communicate()
    communicates.title = request.GET['title']
    communicates.pub_date = timezone.now()
    communicates.body = request.GET['body']
    communicates.save()
    return redirect('layout2')