from django.contrib import admin

# Register your models here.
from .models import People, Media, Images

admin.site.register(People)
admin.site.register(Media)
admin.site.register(Images)
