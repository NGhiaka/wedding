
# Create your models here.
from django.db import models
# from passlib.hash import pbkdf2_sha256
# from django.core.urlresolvers import reverse
# from django.urls import reverse
# from somewhere import handle_uploaded_file
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime
from django.utils.html import escape
from djrichtextfield.models import RichTextField
from django.template.defaultfilters import truncatechars,truncatewords
from cloudinary.models import CloudinaryField



phone_regex = RegexValidator(regex=r'^[0-9]{8,11}$', message="Số điện thoại phải có định dạng 0xxxxxxxxxxx.")

class About(models.Model):
    """docstring for Cosst"""
    """Thông tin vợ chồng
        #name: họ tên
        #ishusban: 1 chong - 0 vo
        #ma code: #Linh: 1904 - Nghia: 0110
    """
    INDEX= (
        ('Trưởng Nam', 'Trưởng Nam'),
        ('Trưởng Nữ', 'Trưởng Nữ'),
        ('Thứ Nam', 'Thứ Nam'),
        ('Thứ Nữ', 'Thứ Nữ'),
        ('Út Nam', 'Út Nam'),
        ('Út Nữ', 'Út Nữ'),
    )
    def __str__(self): 
        return 'Chú Rể' if self.ishusban else 'Cô Dâu'
    name = models.CharField(max_length=200, verbose_name='Họ Tên', default='')
    child_index = models.CharField(max_length=50, verbose_name='Thứ', choices=INDEX, null=True)
    father = models.CharField(max_length=100, verbose_name='Phụ thân', null=True) #tên ba CD-CR
    mother = models.CharField(max_length=100, verbose_name='Mẫu thân', null=True) #tên mẹ CD-CR
    address = models.CharField(max_length=1000, verbose_name='Địa chỉ', null=True) #địa chỉ
    slug = models.SlugField(max_length=500)
    image = CloudinaryField('about')
    # image = models.ImageField(blank = True, verbose_name='Ảnh Đại Diện', upload_to = 'about', default='')
    ishusban = models.BooleanField(default=1, verbose_name='Là Chú Rể')
    code = models.CharField(max_length=10, verbose_name='Mã code', default='') #Linh: 1904 - Nghia: 0110 
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Thêm bởi', default='')
    decription = RichTextField(null=True, blank=True, verbose_name='Giới Thiệu Bản Thân', field_settings='advanced', default='')
    def save(self):
        self.slug = slugify(self.name)
        super(About, self).save()
    @property
    def short_content(self):
        return truncatewords(self.decription, 15)
    class Meta:
        verbose_name = 'envelope'
        verbose_name_plural = "Quản Lý Thông Tin CD-CR"
    
    def image_tag(self):
        return u'<img src="%s" width="150" height="150" />' % escape(self.image)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

class Wedding_Invitation(models.Model): #thiệp cưới
    #Thông tin thiệp cưới
    #Họ tên CDCR
    PARTY= (
        ('Vu Quy', 'Vu Quy'),
        ('Tân Hôn', 'Tân Hôn'),
    )
    
    feast = models.CharField(max_length=100, verbose_name='Lễ', choices=PARTY) #tên đám: Vu Quy - Tân Hôn
    time_calendar = models.DateTimeField('Ngày Dương Lịch') #Ngày dương lịch
    time_lunar = models.DateTimeField('Ngày Âm Lịch') #Ngày âm lịch
    location = models.CharField(blank=True, max_length=500, verbose_name='Địa điểm tổ chức', default='')
    gmap = models.CharField(blank=True, max_length=500, verbose_name='Google map', default='')
    code = models.OneToOneField(About, on_delete=models.CASCADE, verbose_name='Tổ chức tại nhà', default='')
    @property
    def short_content(self):
        return truncatechars(self.gmap, 30)
    class Meta:
        verbose_name = 'envelope'
        verbose_name_plural = "Quản Lý Thiệp Cưới"
    def __str__(self):
        return '%s' % self.feast

class Gallery(models.Model):
    """Bộ sưu tập
    
    """
    title = models.CharField(max_length=200, verbose_name='Bộ sưu tập', default='')
    slug = models.SlugField(max_length=500)
    decription = RichTextField(blank = True, verbose_name='Nội dung', field_settings='advanced', default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    @property
    def short_content(self):
        return truncatewords(self.decription, 20)
    def save(self):
        self.slug = slugify(self.title)
        super(Gallery, self).save()
    def __str__(self):
        return '%s' % self.title
    class Meta:
        verbose_name = 'Khoảnh Khắc'
        verbose_name_plural = "Quản Lý Album"


class Image(models.Model):
    """"""
    path_img = CloudinaryField('gallery') #models.ImageField(blank = True, upload_to = 'gallery', verbose_name='Đường dẫn', default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name='Bộ sưu tập', default='')
    decription = models.CharField(max_length=500, blank = True, verbose_name='Ghi chú', default='')
    slide_show = models.BooleanField(default=1, verbose_name='Ảnh Trình Chiếu')
    class Meta:
        verbose_name = 'Hình Ảnh'
        verbose_name_plural = "Quản Lý Hình Ảnh"
    @property
    def short_content(self):
        return truncatewords(self.decription, 10)
    def image_tag(self):
        return u'<img src="%s" width="150" height="150" />' % escape(self.path_img)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Story(models.Model):
    """
    Câu truyện tình yêu - Blog
    """
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Thêm bởi', default='')
    title = models.CharField(max_length=100, blank = True, verbose_name='Tiêu đề', default='')
    slug = models.SlugField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    images = CloudinaryField('story')   
    # images = models.ImageField(upload_to = 'story', verbose_name='Ảnh đại diện', default='')
    content = RichTextField(blank = True, verbose_name='Nội dung', field_settings='advanced', default='')
    feeling = models.CharField(max_length=100, blank = True, verbose_name='Cảm Nhận', default='')
    def __str__(self):
        return '%s' % self.title
    def save(self):
        self.slug = slugify(self.title)
        super(Story, self).save()
    def __str__(self):
        return '%s' % self.title
    @property
    def short_content(self):
        return truncatewords(self.content, 15)
    class Meta:
        verbose_name = 'Nhật Ký'
        verbose_name_plural = "Quản Lý Nhật Ký"
    def image_tag(self):
        return u'<img src="%s" width="150" height="150" />' % escape(self.images)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Blessing(models.Model):
    """Lời chúc phúc
    name: Họ tên
    blessing: lời chúc
    """
    name = models.CharField(max_length=100, blank = True, verbose_name='Tên khác mời', default='')
    relation = models.CharField(max_length=100, null=True, blank=True, verbose_name='Mối quan hệ')
    blessing = models.TextField(max_length=2000, blank = True, verbose_name='Lời chúc', default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)   

    class Meta:
        verbose_name = 'Lời Chúc'
        verbose_name_plural = "Quản Lý Lời Chúc"
    def __str__(self):
        return '%s' % self.blessing

class Invitee(models.Model):
    """Danh sách khách mời
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guestof = models.ForeignKey(About, on_delete=models.CASCADE, verbose_name='Khách của', default='') #khách của CD hay CR
    name = models.CharField(max_length=100, verbose_name='Tên khách mời', default='') #Tên khách
    phone = models.CharField(validators=[phone_regex], max_length=13, blank=True, verbose_name='Số điện thoại', default='') # Số điện thoại
    address = models.CharField(max_length=100, verbose_name='Địa chỉ', default='') #Địa chỉ
    ivitation = models.BooleanField(default=False, verbose_name='Đã phát thiệp') #đã phát thiệp hay chưa
    adherence_wedding = models.BooleanField(default=False, verbose_name='Đã Đến chung vui') #tham gia lễ cưới hay ko
    money_wedding = models.CharField(max_length=10, default=0, verbose_name='Tiền mừng') #tiền mừng
    class Meta:
        verbose_name = 'Khách Mời'
        verbose_name_plural = "Quản Lý Khách Mời"
    def __str__(self):
        return '%s' % self.user


class Menu(models.Model):
    LINKNAME= (
        ('TRANG CHỦ', 'TRANG CHỦ'),
        ('CÔ DÂU', 'CÔ DÂU'),
        ('CHÚ RỂ', 'CHÚ RỂ'),
        ('NHẬT KÝ', 'NHẬT KÝ'),
        ('TIỆC CƯỚI', 'TIỆC CƯỚI'),
        ('KHOẢNH KHẮC', 'KHOẢNH KHẮC'),
        ('LỜI CHÚC', 'LỜI CHÚC'),
    )
    name = models.CharField(max_length=100, verbose_name='Tên MENU', choices=LINKNAME, default='')
    link = models.SlugField(max_length=200)
    background = CloudinaryField('menu')   
    # background = models.ImageField(upload_to = 'menu', verbose_name='Ảnh Nền', default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Thêm bởi', default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)   
    def save(self):
        self.link = slugify(self.name)
        super(Menu, self).save()
    def __str__(self):
        return '%s' % self.name
    class Meta:
        verbose_name = 'Quản Lý Menu'
        verbose_name_plural = "Quản Lý Menu"
    def image_tag(self):
        if self.background:
            return u'<img src="%s" />' % self.background
        else:
            return '(Sin imagen)'
    image_tag.short_description = 'Ảnh Nền'
    image_tag.allow_tags = True

class Music(models.Model):
    name = models.CharField(max_length=100, verbose_name='Tên Bài Hát', default='')
    slug = models.SlugField(max_length=200)
    link = models.CharField(max_length=2000, verbose_name='Link Nhạc', default='')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Phát Nhạc Ở')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Thêm bởi')
    uploaded_at = models.DateTimeField(auto_now_add=True)  
    play_show = models.BooleanField(default=1, verbose_name='Nhạc Nền Slide Show')
    def save(self):
        self.slug = slugify(self.name)
        super(Music, self).save()
    def __str__(self):
        return '%s' % self.name
    @property
    def short_link(self):
        return truncatechars(self.link, 30)
    class Meta:
        verbose_name = 'Quản Lý Nhạc Nền'
        verbose_name_plural = "Quản Lý Nhạc Nền"
    