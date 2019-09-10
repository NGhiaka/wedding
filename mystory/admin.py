from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Nghia&Linh Admin"
admin.site.site_title = "Nghia&Linh ADMIN MANAGE"
admin.site.index_title = "Welcome to ADMIN"

admin.site.register(About)
admin.site.register(Code)
admin.site.register(Wedding_invitation)
admin.site.register(Gallery)
admin.site.register(Image)
admin.site.register(Story)
