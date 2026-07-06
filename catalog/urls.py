from django.urls import path
from django.views.generic import RedirectView

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", views.ProductListView.as_view(), name="home"),
    path("", RedirectView.as_view(pattern_name="catalog:home", permanent=True)),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>", views.ProductDetailView.as_view(), name="product_details"),
    path("add_product", views.ProductCreateView.as_view(), name="add_product"),
]
