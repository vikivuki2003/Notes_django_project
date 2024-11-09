from django.apps import AppConfig


class NotesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notes_app'

    def ready(self):
        import notes_app.signals