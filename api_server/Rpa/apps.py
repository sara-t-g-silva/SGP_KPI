from django.apps import AppConfig


class RpaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Rpa'

    def ready(self):
        import Rpa.signals
