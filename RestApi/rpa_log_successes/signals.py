from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models

@receiver(post_save,sender=models.RpaLogSuccess)
def update_full_time(sender, instance, created, **kwargs):
    if created:
        
        rpa_instance = instance.rpa
        rpa_instance.duration += instance.duration
        rpa_instance.save()