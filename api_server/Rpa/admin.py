from django.contrib import admin
from Rpa.models import (
    Rpa_model, 
    Log_rpa_model,
    Log_rpa_error_model)
#from Log_rpa.models import Log_rpa

@admin.register(Rpa_model)
class rpaAdmin(admin.ModelAdmin):

    list_display = ('id','name','rpa_status','description','version')
    search_fields = ('name','rpa_status')
    list_filter = ['rpa_status']


    def __str__(self):
        return 
        self.name,
        self.rpa_status,
        self.description, 
        self.version


@admin.register(Log_rpa_model)
class log_rpaAdmin(admin.ModelAdmin):

    list_display = ('id','rpa_id','start_time','end_time','formatted_duration','rpa_log_status','message','created_at','update_at')
    list_filter = ['rpa_log_status']

    def __str__(self):
        return 
        self.id,
        self.rpa_id,
        self.start_time, 
        self.end_time,
        self.formatted_duration,
        self.rpa_log_status,
        self.message,ss
        self.created_at,
        self.update_at


@admin.register(Log_rpa_error_model)
class log_rpa_errorAdmin(admin.ModelAdmin):

    list_display = ('id','rpa_id','start_time','end_time','formatted_duration','rpa_log_status','message','created_at','update_at')
    list_filter = ['rpa_log_status']

    def __str__(self):
        return 
        self.id,
        self.rpa_id,
        self.start_time, 
        self.end_time,
        self.formatted_duration,
        self.rpa_log_status,
        self.message,
        self.created_at,
        self.update_at


    