from django.contrib import admin
from .models import DigitalFiles
# Register your models here.
class DigitalFilesAdmin(admin.ModelAdmin):
    readonly_fields=('Created',)
admin.site.register(DigitalFiles, DigitalFilesAdmin)
