from datetime import timedelta

from django.http import HttpRequest
from django.template import Context
from django.utils import timezone
from misago.plugins.outlets import (
    PluginOutlet,
    append_outlet_action,
    template_outlet_action,
)
from misago.users.models import Online


@template_outlet_action
def users_online_card(request: HttpRequest, context: Context):
    if not request.user.is_staff:
        return None

    users_online = Online.objects.filter(
        last_click__gte=timezone.now() - timedelta(minutes=15),
    ).select_related("user")

    return (
        "misago_users_online_plugin/users_online_card.html",
        {"users_online": users_online},
    )


append_outlet_action(PluginOutlet.CATEGORIES_LIST_END, users_online_card)