from django.contrib import admin
from models import *


class essayAdmin(admin.ModelAdmin):
    list_display = ['title', 'time']

admin.site.register(EssayInfo, essayAdmin)

