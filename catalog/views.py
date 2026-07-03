from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from catalog.forms import ProductForm
from catalog.models import Feedback, Product
from catalog.utils import get_contacts, get_recent_products


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    """
    Display the home page of the catalog app.

    Template:
        catalog/home.html

    Arguments:
        request (HttpRequest): the incoming client request object

    Returns:
        HttpResponse: the fully rendered HTML page
    """
    # recent_products = get_recent_products()
    # print(recent_products)
    # return render(request, "catalog/home.html", context={"recent_products": recent_products})
    products_all = Product.objects.all()

    paginator = Paginator(products_all, 4)
    page_number = request.GET.get("page", 1)
    products = paginator.get_page(page_number)
    return render(request, "catalog/home.html", context={"products": products})


def contacts(request: HttpRequest) -> HttpResponse:
    """
    Display the contacts page of the catalog app and handle the submission of "Contact us" form

    If the request is a GET, it renders the contacts page.
    If the request is a POST, it displays confirmation message.


    Template:
        catalog/contacts.html

    Arguments:
        request (HttpRequest): the incoming client request object

    Returns:
        HttpResponse: the fully rendered contacts HTML page or a page with submission confirmation
    """
    contacts_info = get_contacts()
    if request.method == "POST":
        username = request.POST.get("name", "")
        user_phone = request.POST.get("phone", "")
        feedback_message = request.POST.get("message", "")
        messages.success(request, f"Спасибо {username}, Ваше сообщение получено.")
        Feedback.objects.create(
            feedback_username=username, feedback_phone=user_phone, feedback_message=feedback_message
        )
        return render(request, "catalog/contacts.html", context={"contacts_info": contacts_info})
    return render(request, "catalog/contacts.html", context={"contacts_info": contacts_info})


def product_details(request: HttpRequest, pk: int) -> HttpResponse:
    product = get_object_or_404(Product, pk=pk)
    return render(request, "catalog/product.html", context={"product": product})


def add_product(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = ProductForm()

    return render(request, "catalog/add_product.html", {"form": form})
