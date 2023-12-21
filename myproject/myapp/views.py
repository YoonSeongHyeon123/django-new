from django.shortcuts import render
from .models import Blog
from .models import notice
# Create your views here.

def layout(request):
    return render(request,'myapp/layout.html')

def layout2(request):
    return render(request,'myapp/layout2.html')

def layout3(request):
    notices = notice.objects
    return render(request,'myapp/layout3.html', {'notices':notices})

def layout4(request):
    blogs = Blog.objects
    return render(request,'myapp/layout4.html', {'blogs':blogs})