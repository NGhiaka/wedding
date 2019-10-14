from django.shortcuts import render, redirect
from django.http import HttpResponse
from mystory.models import *
from mystory.forms import BlessingForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request, code=1):
	menu = Menu.objects.get(link='trang-chu')
	musics = Music.objects.filter(menu=menu)
	# about = About.objects.all()
	weddings = Wedding_Invitation.objects.order_by("-id").all()
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
	#pagination
	story_list = Story.objects.order_by('-uploaded_at').all()
	page = request.GET.get('page', 1)
	paginator = Paginator(story_list, 5)
	try:
		stories = paginator.page(page)
	except PageNotAnInteger:
		stories = paginator.page(1)
	except EmptyPage:
		stories = paginator.page(paginator.num_pages)
	context = {
		'menu': menu,
		'musics':musics,
		'stories':stories,
	}
	return render(request, 'wedding/story.html', context)

def Invitation(request):
	menu = Menu.objects.get(link='tiec-cuoi')
	musics = Music.objects.filter(menu=menu)
	weddings = Wedding_Invitation.objects.all()
	context = {
		'menu': menu,
		'musics':musics,
		'weddings':weddings,
	}
	return render(request, 'wedding/invitation.html', context)

def Galleries(request):
	menu = Menu.objects.get(link='khoanh-khac')
	musics = Music.objects.filter(menu=menu)
	galleries = Gallery.objects.order_by('-uploaded_at').all()[:10]
	#pagination
	image_list = Image.objects.order_by('-uploaded_at').all()
	page = request.GET.get('page', 1)
	paginator = Paginator(image_list, 20)
	try:
		images = paginator.page(page)
	except PageNotAnInteger:
		images = paginator.page(1)
	except EmptyPage:
		images = paginator.page(paginator.num_pages)
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
			msg = "Cảm ơn lời chúc tốt đẹp của " + form.cleaned_data['relation'].split()[0] + "!"
			# return redirect('/loi-chuc/')
	form = BlessingForm()
	menu = Menu.objects.get(link='loi-chuc')
	musics = Music.objects.filter(menu=menu)
	#pagination
	blessings = Blessing.objects.order_by('-uploaded_at').all()
	# page = request.GET.get('page', 1)
	# paginator = Paginator(blessing_list, 2)
	# try:
	# 	blessings = paginator.page(page)
	# except PageNotAnInteger:
	# 	blessings = paginator.page(1)
	# except EmptyPage:
	# 	blessings = paginator.page(paginator.num_pages)
	context = {
		'menu': menu,
		'musics':musics,
		'blessings':blessings,
		'msg': msg,
		'form': form
	}

	return render(request, 'wedding/blessing.html', context)

def handler404(request):
    return render(request, 'wedding/error_page/404.html', status=404)

def handler500(request):
    return render(request, 'wedding/error_page/404.html', status=500)