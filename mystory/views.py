from django.shortcuts import render
from django.http import HttpResponse
from mystory.models import *

# Create your views here.

def index(request, code=1):
	menu = Menu.objects.get(link='trang-chu')
	# about = About.objects.all()
	weddings = Wedding_Invitation.objects.all()
	context = {
		'menu': menu,
		# 'about':about,
		'weddings': weddings
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

def Stories(request):
	menu = Menu.objects.get(link='nhat-ky')
	stories = Story.objects.order_by('-uploaded_at').all()[:5]
	context = {
		'menu': menu,
		'stories':stories,
	}
	return render(request, 'wedding/story.html', context)

def Invitation(request):
	menu = Menu.objects.get(link='tiec-cuoi')
	invitations = Wedding_Invitation.objects.all()
	context = {
		'menu': menu,
		'invitations':invitations,
	}
	return render(request, 'wedding/invitation.html', context)

def Galleries(request):
	menu = Menu.objects.get(link='khoanh-khac')
	galleries = Gallery.objects.order_by('-uploaded_at').all()[:5]
	images = Image.objects.order_by('-uploaded_at').all()[:30]
	context = {
		'menu': menu,
		'galleries':galleries,
		'images':images
	}
	return render(request, 'wedding/gallery.html', context)

# def Journal(request):
# 	return render(request, 'wedding/story.html')

def Blessings(request):
	menu = Menu.objects.get(link='loi-chuc')
	blessings = Blessing.objects.all()
	context = {
		'menu': menu,
		'blessings':blessings,
	}
	return render(request, 'wedding/blessing.html',context)