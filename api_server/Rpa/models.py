from django.db import models
from datetime import timedelta

# Create your models here.
class Rpa_model(models.Model):

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





class Log_rpa_model(models.Model):
    
    rpa_id = models.ForeignKey(Rpa_model, on_delete=models.CASCADE, related_name='rpa_id')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField(default=0,null=True, blank=True)
    rpa_log_status = models.CharField(max_length=50, choices=[('success','Success')])
    #retornar a mensagem de erro ou não
    message = models.TextField(null=True,blank=True)

    #rastrear a criação no banco de dados e a inclusão do registro

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    #banco de dados relacional para retornar log de RPA específico

    def formatted_duration(self):
        if self.duration:

            total_seconds = int(self.duration.total_seconds())
            hours, remaider = divmod(total_seconds,3600)
            minutes, seconds = divmod(remaider,60)
            return f'{hours}h {minutes}m {seconds}s'

        return "N/A"

    formatted_duration.short_description = 'Duration'


class Log_rpa_error_model(models.Model):
    rpa_id = models.ForeignKey(Rpa_model, on_delete=models.CASCADE, related_name='rpa_id_error')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField(null=True, blank=True)
    rpa_log_status = models.CharField(max_length=50, choices=[('fault','Fault')])
    #retornar a mensagem de erro ou não
    message = models.TextField(null=True,blank=True)

    #rastrear a criação no banco de dados e a inclusão do registro

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    #banco de dados relacional para retornar log de RPA específico
   

    def formatted_duration(self):
        if self.duration:

            total_seconds = int(self.duration.total_seconds())
            hours, remaider = divmod(total_seconds,3600)
            minutes, seconds = divmod(remaider,60)
            return f'{hours}h {minutes}m {seconds}s'

        return "N/A"

    formatted_duration.short_description = 'Duration'






