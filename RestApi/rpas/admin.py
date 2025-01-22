from django.contrib import admin
from rpas.models import Rpa


class RpaAdmin(admin.ModelAdmin):
    list_display = ('name','description',)
    search_fields = ('name',)

admin.site.register(Rpa, RpaAdmin)


