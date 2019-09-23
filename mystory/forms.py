from django import forms
from django.forms import ModelForm
from django.contrib import admin
from mystory.models import Blessing
# from myapp.widgets import RichTextEditorWidget

RELATION = (
        ('Bạn Cô Dâu', 'Bạn Cô Dâu'),
        ('Anh Cô Dâu', 'Anh Cô Dâu'),
        ('Chị Cô Dâu', 'Chị Cô Dâu'),
        ('Em Cô Dâu', 'Em Cô Dâu'),
        ('Cháu Cô Dâu', 'Cháu Cô Dâu'),
        ('Cô Cô Dâu', 'Bạn Cô Dâu'),
        ('Dì Cô Dâu', 'Dì Cô Dâu'),
        ('Chú Cô Dâu', 'Chú Cô Dâu'),
        ('Bác Cô Dâu', 'Bác Cô Dâu'),
        ('Cậu Cô Dâu', 'Cậu Cô Dâu'),
        ('Ông Cô Dâu', 'Ông Cô Dâu'),
        ('Bà Cô Dâu', 'Bà Cô Dâu'),
        ('Bạn Chú Rể', 'Bạn Chú Rể'),
        ('Anh Chú Rể', 'Anh Chú Rể'),
        ('Chị Chú Rể', 'Chị Chú Rể'),
        ('Em Chú Rể', 'Em Chú Rể'),
        ('Cháu Chú Rể', 'Cháu Chú Rể'),
        ('Cô Chú Rể', 'Bạn Chú Rể'),
        ('Dì Chú Rể', 'Dì Chú Rể'),
        ('Chú Chú Rể', 'Chú Chú Rể'),
        ('Bác Chú Rể', 'Bác Chú Rể'),
        ('Cậu Chú Rể', 'Cậu Chú Rể'),
        ('Ông Chú Rể', 'Ông Chú Rể'),
        ('Bà Chú Rể', 'Bà Chú Rể'),
        ('Mợ Chú Rể', 'Mợ Chú Rể'),
        ('Thím Chú Rể', 'Thím Chú Rể'),
        ('Dượng Chú Rể', 'Dượng Chú Rể')
    )
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
			'relation': forms.Select(choices = RELATION, attrs={'class': 'form-control','placeholder': 'Mối quan hệ với CD-CR', 'name': 'relation'}),			
			'blessing': forms.Textarea(attrs={'cols': 30, 'rows': 5, 'class': 'form-control','placeholder': 'Lời chúc cho cô dâu và chú rể',  'name': 'blessing'}),
        }