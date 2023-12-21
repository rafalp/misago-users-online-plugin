from django.apps import AppConfig


class MisagoUsersOnlinePlugin(AppConfig):
    name = "misago_users_online_plugin"

    def ready(self):
        from . import online_card