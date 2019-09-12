from django.contrib import admin
from .models import *

 

# Register your models here.
admin.site.site_header = "Admin"
admin.site.site_title = "ADMIN MANAGE"
admin.site.index_title = "Welcome to ADMIN"

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    fields = ('name', 'ishusban', 'code')
    ordering = ('name',)
    search_fields = ('name',)

# admin.site.register(About)
admin.site.register(Wedding_Invitation)
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    fields = ('title', 'decription' )
    ordering = ('title',)
    search_fields = ('title',)
# admin.site.register(Gallery)
admin.site.register(Image)
@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    fields = ('title', 'images', 'content' )
    ordering = ('title',)
    search_fields = ('title',)
# admin.site.register(Story)
# admin.site.register(Invitee)
@admin.register(Invitee)
class InviteeAdmin(admin.ModelAdmin):
    fields = ('name', 'phone', 'address','guestof', 'ivitation', 'adherence_wedding', 'money_wedding')
    ordering = ('name','guestof', 'ivitation', 'adherence_wedding')
    search_fields = ('name','phone', 'address')
# admin.site.register(Story)
