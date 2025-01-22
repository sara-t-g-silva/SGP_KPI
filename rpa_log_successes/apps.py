from django.apps import AppConfig


class RpaLogSuccessesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rpa_log_successes'


    def ready(self):
        import rpa_log_successes.signals