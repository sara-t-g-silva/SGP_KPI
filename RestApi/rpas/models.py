from django.db import models
from datetime import timedelta




class Rpa(models.Model):

    #id gerado automaticamente pelo django
    
    #name
    name = models.CharField(max_length=255,blank=True)
    #status
    rpa_status = models.CharField(max_length=50, choices=[('running','Running'),('stopped','Stopped')], default='stopped')
    #descrição rápida
    description = models.TextField(blank=True,null=True)
    #versão do rpa que foi rodado, v1, v2
    version = models.CharField(max_length=50,blank=True,null=True)
    #tempo total rodando
    duration = models.DurationField(default=timedelta(hours=0),null=True, blank=True)
    #quantidade de erros 
    error_count = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at =  models.DateTimeField(auto_now=True)


    def formatted_duration(self):
        if self.duration:

            total_seconds = int(self.duration.total_seconds())
            hours, remaider = divmod(total_seconds,3600)
            minutes, seconds = divmod(remaider,60)
            return f'{hours}h {minutes}m {seconds}s'

        return "N/A"

    formatted_duration.short_description = 'Duration'

    #ordena por nome
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    


    
