from django.shortcuts import render, redirect
from django.http import HttpResponse
from mystory.models import *
from mystory.forms import BlessingForm

# Create your views here.

def index(request, code=1):
	menu = Menu.objects.get(link='trang-chu')
	musics = Music.objects.filter(menu=menu)
	# about = About.objects.all()
	weddings = Wedding_Invitation.objects.all()
	context = {
		'menu': menu,
		'musics':musics,
		'weddings': weddings
	}
	return render(request, 'wedding/index.html', context)

def About_Her(request):
	menu = Menu.objects.get(link='co-dau')
	musics = Music.objects.filter(menu=menu)
	about = About.objects.get(ishusban=False)
	context = {
		'menu': menu,
		'musics':musics,
		'about':about,
	}
	return render(request, 'wedding/about_her.html', context)

def About_Him(request):
	menu = Menu.objects.get(link='chu-re')
	musics = Music.objects.filter(menu=menu)
	about = About.objects.get(ishusban=True)
	context = {
		'menu': menu,
		'musics':musics,
		'about':about,
	}
	return render(request, 'wedding/about_him.html',context)

def Stories(request):
	menu = Menu.objects.get(link='nhat-ky')
	musics = Music.objects.filter(menu=menu)
	stories = Story.objects.order_by('-uploaded_at').all()[:5]
	context = {
		'menu': menu,
		'musics':musics,
		'stories':stories,
	}
	return render(request, 'wedding/story.html', context)

def Invitation(request):
	menu = Menu.objects.get(link='tiec-cuoi')
	musics = Music.objects.filter(menu=menu)
	invitations = Wedding_Invitation.objects.all()
	context = {
		'menu': menu,
		'musics':musics,
		'invitations':invitations,
	}
	return render(request, 'wedding/invitation.html', context)

def Galleries(request):
	menu = Menu.objects.get(link='khoanh-khac')
	musics = Music.objects.filter(menu=menu)
	galleries = Gallery.objects.order_by('-uploaded_at').all()[:10]
	images = Image.objects.order_by('-uploaded_at').all()[:50]
	context = {
		'menu': menu,
		'musics':musics,
		'galleries':galleries,
		'images':images
	}
	return render(request, 'wedding/gallery.html', context)

# def Journal(request):
# 	return render(request, 'wedding/story.html')

def Blessings(request):
	msg = None
	if request.method == 'POST':
		form = BlessingForm(request.POST)
		if form.is_valid():
			form.save()
			msg = "Cảm ơn bạn đã bỏ chút thời gian để dành những lời chúc tốt đẹp dành cho cô dâu-chú rể!"
			# return redirect('/loi-chuc/')
	form = BlessingForm()
	menu = Menu.objects.get(link='loi-chuc')
	musics = Music.objects.filter(menu=menu)
	blessings = Blessing.objects.order_by('-uploaded_at').all()[:20] 
	context = {
		'menu': menu,
		'musics':musics,
		'blessings':blessings,
		'msg': msg,
		'form': form
	}

	return render(request, 'wedding/blessing.html', context)