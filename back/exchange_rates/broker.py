from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = "my_app"
    verbose_name = "My App"

    def ready(self):
        # TODO: Write your codes to run on startup
        pass
