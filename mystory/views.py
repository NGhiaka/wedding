from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'wedding/index.html')

def About_Her(request):
    return render(request, 'wedding/about_her.html')

def About_Him(request):
	return render(request, 'wedding/about_him.html')

def Story(request):
    return render(request, 'wedding/story.html')

def Invitation(request):
	return render(request, 'wedding/invitation.html')

def Gallery(request):
	return render(request, 'wedding/gallery.html')

# def Journal(request):
# 	return render(request, 'wedding/story.html')

def Blessing(request):
	return render(request, 'wedding/blessing.html')