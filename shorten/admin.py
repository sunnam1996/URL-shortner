from django.contrib import admin

# Register your models here.
from .models import ShortURL

class ShortURLAdmin(admin.ModelAdmin):
    list_display   = ('url', 'code', 'date', 'nb_access')
    date_hierarchy = 'date'
    ordering       = ('date',)
    search_fields  = ('url',)

admin.site.register(ShortURL, ShortURLAdmin)