from django.contrib import admin
from port.models import Port

# Register your models here.
@admin.register(Port)
class PortAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')