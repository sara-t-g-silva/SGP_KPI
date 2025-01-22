from django.apps import AppConfig


class RpaLogErrorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rpa_log_errors'

    def ready(self):
        import rpa_log_errors.signals