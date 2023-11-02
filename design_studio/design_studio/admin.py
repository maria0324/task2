from django.contrib import admin

# Register your models here.

from .models import AdvUser, Request

admin.site.register(AdvUser)
admin.site.register(Request)