from django.apps import AppConfig

class AlertsAppConfig(AppConfig):
    name = 'alerts'
    verbose_name = 'Envio de Alertas'

    def ready(self):
        from . import signals
