from django.apps import AppConfig

class learningConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'learning'
    
    def ready(self):
        # Importing the signals
        import learning.signals