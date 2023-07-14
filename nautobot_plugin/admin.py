from django.contrib import admin
from .models import Components

class ComponentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
