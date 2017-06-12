from django.contrib import admin
from models import *


class essayAdmin(admin.ModelAdmin):
    list_display = ['title', 'time']


class contactAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'phone']


admin.site.register(EssayInfo, essayAdmin)
admin.site.register(ContactInfo, contactAdmin)
