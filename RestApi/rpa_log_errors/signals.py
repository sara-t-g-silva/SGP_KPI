from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from . import models

@receiver(post_save,sender=models.RpaLogError)
def update_error_count(sender,instance,created,**kwargs):
    if created:
        rpa_instance = instance.rpa
        rpa_instance.error_count = rpa_instance.error_count + 1
        rpa_instance.save()
        

