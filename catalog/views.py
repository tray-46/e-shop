from typing import Any

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from catalog.forms import FeedbackForm, ProductForm
from catalog.models import Product
from catalog.utils import get_contacts


# Create your views here.
class ProductListView(ListView):
    model = Product
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self) -> str:
        return reverse("catalog:product_detail", kwargs={"pk": self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")

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
