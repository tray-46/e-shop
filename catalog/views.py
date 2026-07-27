from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.http import HttpResponse, HttpResponseForbidden, HttpRequest, Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView

from catalog.forms import FeedbackForm, ProductForm
from catalog.models import Product
from catalog.utils import get_contacts


# Create your views here.
class ProductListView(ListView):
    model = Product
    paginate_by = 4

    def get_queryset(self) -> QuerySet[Product]:
        return Product.objects.filter(is_published=True)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["page"] = self.request.GET.get("page", 1)
        return context

    def get_object(self, queryset: QuerySet[Product] = None) -> Product:
        obj = super().get_object(queryset)
        if not obj.is_published:
            raise Http404("No such product available")
        return obj


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        print(self.request.GET)
        context["page"] = self.request.GET.get("page", 1)
        print(context["page"])
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user

    def get_success_url(self) -> str:
        return reverse("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user or self.request.user.has_perm("catalog.delete_product")

class ProductUnpublishView(LoginRequiredMixin, UserPassesTestMixin, View):
    """"""

    def test_func(self) -> bool:
        return self.request.user.has_perm("catalog.can_unpublish_product")

    def post(self, request, pk):
        if not self.request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden()

        product = get_object_or_404(Product, pk=pk)
        product.is_published = False
        product.save()
        return redirect("catalog:home")


class ContactsView(SuccessMessageMixin, FormView):
    template_name = "catalog/contacts.html"
    form_class = FeedbackForm
    success_url = reverse_lazy("catalog:contacts")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        contacts_info = get_contacts()
        context["contacts_info"] = contacts_info
        return context

    def form_valid(self, form: FeedbackForm) -> HttpResponse:
        form.save()
        username = form.cleaned_data.get("feedback_username", "")
        success_message = f"Спасибо {username}, Ваше сообщение получено."
        messages.success(self.request, success_message)
        return super().form_valid(form)
