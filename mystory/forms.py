from django import forms
from django.forms import ModelForm
from django.contrib import admin
from mystory.models import *
# from myapp.widgets import RichTextEditorWidget

class StoryAdmin(admin.ModelAdmin):  
	"""docstring for Contacts
    title = models.CharField(max_length=100, blank = True)
    slug = models.SlugField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)   
    images = models.ImageField(upload_to = 'story/%Y/%m/%d')
    content = models.CharField(max_length=5000, blank = True)
    """
	class Meta:
		model = Story
		fields = ['title','images', 'content']
		labels = {
			'title' : 'Tiêu đề',
			'images': 'Ảnh',
			'content' : 'Nội dung'
		}
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tiêu đề', 'name': 'title'}),
			'images': forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control','placeholder': 'Ảnh', 'name': 'images'}),			
			'decription': forms.Textarea(attrs={'cols': 30, 'rows': 5, 'class': 'form-control','placeholder': 'Câu truyện tình yêu',  'name': 'decription'}),
        }