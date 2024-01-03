from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Blog
from .models import notice
from .models import communicate
from .forms import CreateForm
# Create your views here.

def layout(request):
    return render(request,'myapp/layout.html')

def layout2(request):
    communicates = communicate.objects
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('layout2')
    else:
        form = CreateForm()
        return render(request, 'myapp/layout2.html', {'form':form, 'communicates':communicates})

def layout3(request):
    notices = notice.objects
    return render(request,'myapp/layout3.html', {'notices':notices})

def layout4(request):
    blogs = Blog.objects
    return render(request,'myapp/layout4.html', {'blogs':blogs})