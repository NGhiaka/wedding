from django import forms
from django.forms import ModelForm
from django.contrib import admin
from mystory.models import Blessing
# from myapp.widgets import RichTextEditorWidget

class BlessingForm(ModelForm):  
	"""docstring for Contacts
    title = models.CharField(max_length=100, blank = True)
    slug = models.SlugField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)   
    images = models.ImageField(upload_to = 'story/%Y/%m/%d')
    content = models.CharField(max_length=5000, blank = True)
    """
	class Meta:
		model = Blessing
		fields = ['name','relation', 'blessing']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tên khách mời', 'name': 'name'}),
			'relation': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Mối quan hệ với CD-CR', 'name': 'relation'}),			
			'blessing': forms.Textarea(attrs={'cols': 30, 'rows': 5, 'class': 'form-control','placeholder': 'Lời chúc cho cô dâu và chú rể',  'name': 'blessing'}),
        }