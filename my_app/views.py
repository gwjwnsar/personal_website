from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'my_app/index.html', {})

def about(request):
    return render(request, 'my_app/about.html', {})

def resume(request):
    return render(request, 'my_app/resume.html', {})

def contact(request):
    return render(request, 'my_app/contact.html', {})
