from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="catalog:home", permanent=True)),
    path("home/", views.ProductListView.as_view(), name="home"),
    path("product/<int:pk>/", cache_page(60)(views.ProductDetailView.as_view()), name="product_detail"),
    path("product/new/", views.ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/edit/", views.ProductUpdateView.as_view(), name="product_edit"),
    path("product/<int:pk>/unpublish/", views.ProductUnpublishView.as_view(), name="product_unpublish"),
    path("product/<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("category/<int:pk>/", views.CategoryProductsListView.as_view(), name="category_products"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
]
