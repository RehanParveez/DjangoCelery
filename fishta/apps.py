from django.apps import AppConfig

class FishtaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'fishta'
    
    def ready(self):
        # Importing the signals
        import fishta.signals