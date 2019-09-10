# Create your models here.

# Create your models here.
from django.db import models
# from passlib.hash import pbkdf2_sha256
# from django.core.urlresolvers import reverse
from django.urls import reverse
# from somewhere import handle_uploaded_file
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime


class About(models.Model):
    """docstring for Cosst"""
    """Thông tin vợ chồng
        #name: họ tên
        #ishusban: 1 chong - 0 vo
        #ma code: #Linh: 1904 - Nghia: 0110
    """
    def __str__(self): 
        return self.name
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    ishusban = models.BooleanField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def save(self):
        self.slug = slugify(self.name)
        super(About, self).save()
    class Meta:
        verbose_name_plural = "Thông Tin"

class Code(models.Model):
    """Mã code - 
    """
    code = models.CharField(max_length=10) #Linh: 1904 - Nghia: 0110 
    isWho = models.OneToOneField(About, on_delete=models.CASCADE)  
    class Meta:
        verbose_name_plural = "Mã code"

class Wedding_invitation(models.Model): #thiệp cưới
    #Thông tin thiệp cưới
    #Họ tên cô dâu
    time = models.DateField('date published')
    location = models.CharField(max_length=500)
    code = models.OneToOneField(About, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Thiệp Cưới"

class Gallery(models.Model):
    """Bộ sưu tập
    
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    decription = models.CharField(max_length=200, blank = True)
    uploaded_at = models.DateTimeField(auto_now_add=True)   
    def save(self):
        self.slug = slugify(self.title)
        super(Gallery, self).save()
    def __str__(self):
        return '%s' % self.title
    class Meta:
        verbose_name_plural = "Tên Album"

class Image(models.Model):
    """"""
    path_img = models.ImageField(blank = True, upload_to = 'gallery/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    decription = models.CharField(max_length=50000, blank = True)
    class Meta:
        verbose_name_plural = "Hình Ảnh"

class Story(models.Model):
    """
    Câu truyện tình yêu - Blog
    """
    title = models.CharField(max_length=100, blank = True)
    slug = models.SlugField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)   
    images = models.ImageField(upload_to = 'story/%Y/%m/%d')
    def save(self):
        self.slug = slugify(self.title)
        super(Story, self).save()
    def __str__(self):
        return '%s' % self.title
    class Meta:
        verbose_name_plural = "Câu Chuyện Tình Yêu"

class Blessing(models.Model):
    """Lời chúc phúc
    """
    name = models.CharField(max_length=100, blank = True)
    blessing = models.CharField(max_length=1000, blank = True)
    class Meta:
        verbose_name_plural = "Lời Chúc"

