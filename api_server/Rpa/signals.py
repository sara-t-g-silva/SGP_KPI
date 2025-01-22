from django.db.models.signals import post_save
from django.dispatch import receiver
from Rpa.models import (
    Log_rpa_error_model, 
    Rpa_model, 
    Log_rpa_model)

@receiver(post_save, sender=Log_rpa_error_model)
def update_error_count(sender, instance,created,**kwargs):
    #verifica se a intância de log_rpa_error_model foi criada, se sim entra no if e atualiza as informações que deseja
    if created:
       

        rpa_instance = instance.rpa_id
        rpa_instance.error_count = rpa_instance.error_count +1
        rpa_instance.save()
        

@receiver(post_save, sender=Log_rpa_model)    
def update_full_time(sender, instance, created,**kwargs):
    if created:
        Rpa_model = instance.rpa_id
        Rpa_model.duration += instance.duration
        Rpa_model.save()
        


