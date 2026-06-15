from django.urls import path
from django.views.generic import RedirectView
from catalog.apps import CatalogConfig
from . import views


app_name = CatalogConfig.name

urlpatterns = [
    path("home/", views.home, name="home"),
    path("", RedirectView.as_view(pattern_name="catalog:home", permanent=True)),
    path("contacts/", views.contacts, name="contacts" ),
]