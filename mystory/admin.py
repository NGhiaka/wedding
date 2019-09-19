from django.contrib import admin
from .models import *

 

# Register your models here.
admin.site.site_header = "Wedding"
admin.site.site_title = "ADMIN MANAGE"
admin.site.index_title = "Welcome to ADMIN"

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)
    list_display = ('name', 'ishusban', 'image_tag', 'code', 'user')
    fields = ('name', 'ishusban','image', 'code', 'decription')
    ordering = ('name',)
    search_fields = ('name', 'code', 'user')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

# admin.site.register(About)
# admin.site.register(Wedding_Invitation)
@admin.register(Wedding_Invitation)
class Wedding_InvitationAdmin(admin.ModelAdmin):
    list_display = ('code', 'location', 'feast', 'time_calendar', 'time_lunar')
    fields = ('code', 'location', 'feast', 'time_calendar', 'time_lunar')
    ordering = ('code', 'location', 'feast', 'time_calendar', 'time_lunar')
    search_fields = ('code', 'location', 'feast', 'time_calendar', 'time_lunar')
    

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
    # readonl = ('image_tag',)
    list_display = ('title', 'uploaded_at', 'image_tag', 'user')
    ordering = ('title',)
    search_fields = ('title',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
# admin.site.register(Story)
# admin.site.register(Invitee)
@admin.register(Invitee)
class InviteeAdmin(admin.ModelAdmin):
    fields = ('name', 'phone', 'address','guestof', 'ivitation', 'adherence_wedding', 'money_wedding')
    list_display = ('name', 'phone', 'address','guestof', 'ivitation', 'adherence_wedding', 'money_wedding', 'user')

    ordering = ('name','guestof', 'ivitation', 'adherence_wedding')
    search_fields = ('name','phone', 'address')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
# admin.site.register(Story)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image_tag','uploaded_at', 'user')
    fields = ('name', 'link', 'background')
    # readonly_fields = ('image_tag',)
    ordering = ('name','link', 'user')
    search_fields = ('name',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'link', 'menu','uploaded_at', 'user')
    fields = ('name', 'link', 'menu')
    # readonly_fields = ('image_tag',)
    ordering = ('name', 'user')
    search_fields = ('name',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
