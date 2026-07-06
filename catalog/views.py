from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from catalog.forms import ProductForm, FeedbackForm
from catalog.models import Feedback, Product
from catalog.utils import get_contacts, get_recent_products


# Create your views here.
class ProductListView(ListView):
    model = Product
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ["product_name", "product_description", "image", "product_category", "price",]
    success_url = reverse_lazy("catalog:home")


class ContactsView(SuccessMessageMixin, FormView):
    template_name = "catalog/contacts.html"
    form_class = FeedbackForm
    success_url = reverse_lazy("catalog:contacts")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contacts_info = get_contacts()
        context["contacts_info"] = contacts_info
        return context

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("feedback_username", "")
        success_message = f"Спасибо {username}, Ваше сообщение получено."
        messages.success(self.request, success_message)
        return super().form_valid(form)

