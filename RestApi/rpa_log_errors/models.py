from django.db import models
from rpas.models import Rpa


class RpaLogError(models.Model):

    rpa = models.ForeignKey(Rpa, on_delete=models.CASCADE, related_name='log_error_rpa_id')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField(default=0,null=True, blank=True)
    rpa_log_status = models.CharField(max_length=50, choices=[('fault','Fault')], default='fault')
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