from django.apps import AppConfig


class BoardNewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Board_News'

    def ready(self):
        import Board_News.signals