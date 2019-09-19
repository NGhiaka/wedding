from django.shortcuts import render
from django.http import HttpResponse
from mystory.models import *

# Create your views here.

def index(request, pk=1):
	menu = Menu.objects.get(link='trang-chu')
	about = About.objects.all()
	wedding = Wedding_Invitation.objects.get(code=pk)
	context = {
		'menu': menu,
		'about':about,
		'wedding': wedding
	}
	return render(request, 'wedding/index.html', context)

def About_Her(request):
	menu = Menu.objects.get(link='co-dau')
	about = About.objects.get(ishusban=False)
	context = {
		'menu': menu,
		'about':about,
	}
	return render(request, 'wedding/about_her.html', context)

def About_Him(request):
	menu = Menu.objects.get(link='chu-re')
	about = About.objects.get(ishusban=True)
	context = {
		'menu': menu,
		'about':about,
	}
	return render(request, 'wedding/about_him.html',context)

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