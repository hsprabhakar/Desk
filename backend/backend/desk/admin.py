from django.contrib import admin
from .models import Sticky

class DeskAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'completed')

admin.site.register(Sticky, DeskAdmin)