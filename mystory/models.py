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

phone_regex = RegexValidator(regex=r'^[0-9]{8,11}$', message="Số điện thoại phải có định dạng 0xxxxxxxxxxx.")

class About(models.Model):
    """docstring for Cosst"""
    """Thông tin vợ chồng
        #name: họ tên
        #ishusban: 1 chong - 0 vo
        #ma code: #Linh: 1904 - Nghia: 0110
    """
    def __str__(self): 
        return 'Chú Rể' if self.ishusban else 'Cô Dâu'
    name = models.CharField(max_length=200, verbose_name='Họ Tên')
    slug = models.SlugField(max_length=500)
    ishusban = models.BooleanField(default=1, verbose_name='Là Chú Rể')
    code = models.CharField(max_length=10, verbose_name='Mã code') #Linh: 1904 - Nghia: 0110 
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    def save(self):
        self.slug = slugify(self.name)
        super(About, self).save()
    class Meta:
        verbose_name_plural = "Quản Lý Thông Tin CD-CR"

class Wedding_Invitation(models.Model): #thiệp cưới
    #Thông tin thiệp cưới
    #Họ tên CDCR
    PARTY= (
        ('Vu Quy', 'Vu Quy'),
        ('Tân Hôn', 'Tân Hôn'),
    )
    feast = models.CharField(max_length=100, verbose_name='Lễ', choices=PARTY) #tên đám: Vu Quy - Tân Hôn
    time_calendar = models.DateField('Ngày Dương Lịch') #Ngày dương lịch
    time_lunar = models.DateField('Ngày Âm Lịch') #Ngày âm lịch
    location = models.CharField(max_length=500, verbose_name='Địa điểm tổ chức:')
    code = models.OneToOneField(About, on_delete=models.CASCADE, verbose_name='Tổ chức tại nhà')
    class Meta:
        verbose_name_plural = "Quản Lý Thiệp Cưới"

class Gallery(models.Model):
    """Bộ sưu tập
    
    """
    title = models.CharField(max_length=200, verbose_name='Bộ sưu tập')
    slug = models.SlugField(max_length=500)
    decription = models.CharField(max_length=200, blank = True, verbose_name='Nội dung')
    uploaded_at = models.DateTimeField(auto_now_add=True)   
    def save(self):
        self.slug = slugify(self.title)
        super(Gallery, self).save()
    def __str__(self):
        return '%s' % self.title
    class Meta:
        verbose_name_plural = "Quản Lý Album"

class Image(models.Model):
    """"""
    path_img = models.ImageField(blank = True, upload_to = 'gallery/%Y/%m/%d', verbose_name='Đường dẫn')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name='Bộ sưu tập')
    decription = models.CharField(max_length=50000, blank = True, verbose_name='Ghi chú')
    class Meta:
        verbose_name_plural = "Quản Lý Hình Ảnh"

class Story(models.Model):
    """
    Câu truyện tình yêu - Blog
    """
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, blank = True, verbose_name='Tiêu đề')
    slug = models.SlugField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)   
    images = models.ImageField(upload_to = 'story/%Y/%m/%d', verbose_name='Ảnh đại diện')
    content = models.CharField(max_length=5000, blank = True, verbose_name='Nội dung')
    def save(self):
        self.slug = slugify(self.title)
        super(Story, self).save()
    def __str__(self):
        return '%s' % self.title
    class Meta:
        verbose_name_plural = "Câu Chuyện Tình Yêu"

class Blessing(models.Model):
    """Lời chúc phúc
    name: Họ tên
    blessing: lời chúc
    """
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, blank = True, verbose_name='Tên khác mời')
    blessing = models.CharField(max_length=1000, blank = True, verbose_name='Lời chúc')
    class Meta:
        verbose_name_plural = "Lời Chúc"

class Invitee(models.Model):
    """Danh sách khách mời
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guestof = models.ForeignKey(About, on_delete=models.CASCADE, verbose_name='Khách của') #khách của CD hay CR
    name = models.CharField(max_length=100, verbose_name='Tên khách mời') #Tên khách
    phone = models.CharField(validators=[phone_regex], max_length=13, blank=True, verbose_name='Số điện thoại') # Số điện thoại
    address = models.CharField(max_length=100, verbose_name='Địa chỉ') #Địa chỉ
    ivitation = models.BooleanField(default=False, verbose_name='Đã phát thiệp') #đã phát thiệp hay chưa
    adherence_wedding = models.BooleanField(default=False, verbose_name='Đã Đến chung vui') #tham gia lễ cưới hay ko
    money_wedding = models.CharField(max_length=10, default=0, verbose_name='Tiền mừng') #tiền mừng
    class Meta:
        verbose_name_plural = "Quản Lý Khách Mời"

