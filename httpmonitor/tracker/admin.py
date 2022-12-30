from django.contrib import admin

from .models import Address, Request

admin.site.register(Address)
admin.site.register(Request)