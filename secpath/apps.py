from django.apps import AppConfig


class SecpathConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'secpath'

    # def ready(self):
        # from .tasks import clean_expired_records
        # clean_expired_records()