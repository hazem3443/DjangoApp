from django.apps import AppConfig


class AccountssConfig(AppConfig):
    name = 'accountss'

    def ready(self):
        import accountss.signals
