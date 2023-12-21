from django.urls import path

from . import views

app_name = "users-online-plugin"
urlpatterns = [
    path("users-online/", views.index, name="index"),
]