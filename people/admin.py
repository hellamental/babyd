from django.contrib import admin

# Register your models here.
from .models import People, Media

admin.site.register(People)
admin.site.register(Media)