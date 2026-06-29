from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import RedirectView

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", views.home, name="home"),
    path("", RedirectView.as_view(pattern_name="catalog:home", permanent=True)),
    path("contacts/", views.contacts, name="contacts"),
    path("products/<int:pk>", views.product_details, name="product_details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
