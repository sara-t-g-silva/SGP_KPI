from django.contrib import admin
from . import models


class RpaLogSuccessAdmin(admin.ModelAdmin):
    list_display = ('rpa','duration','rpa_log_status','message',)
    search_fields = ('rpa',)

admin.site.register(models.RpaLogSuccess, RpaLogSuccessAdmin)
