from django.contrib import admin
from .models import *

 

# Register your models here.
admin.site.site_header = "Quản Lý Đám Cưới"
admin.site.site_title = "ADMIN MANAGE"
admin.site.index_title = "Welcome to ADMIN"

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    fields = ('name', 'ishusban','avatar', 'code')
    ordering = ('name',)
    search_fields = ('name', 'avatar', 'code', 'ishusban', 'user')
    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)

# admin.site.register(About)
admin.site.register(Wedding_Invitation)

class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    fields = ('title', 'decription' )
    ordering = ('title',)
    search_fields = ('title',)
    inlines = [
        ImageInline,
    ]
# admin.site.register(Gallery)
# admin.site.register(Image)

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    fields = ('title', 'images', 'content' )
    ordering = ('title',)
    search_fields = ('title',)
    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)
# admin.site.register(Story)
# admin.site.register(Invitee)
@admin.register(Invitee)
class InviteeAdmin(admin.ModelAdmin):
    fields = ('name', 'phone', 'address','guestof', 'ivitation', 'adherence_wedding', 'money_wedding')
    ordering = ('name','guestof', 'ivitation', 'adherence_wedding')
    search_fields = ('name','phone', 'address')
    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)
# admin.site.register(Story)
