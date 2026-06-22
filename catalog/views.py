from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from catalog.models import Product
from catalog.utils import get_recent_products


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
    recent_products = get_recent_products()
    print(recent_products)
    return render(request, "catalog/home.html", context={"recent_products": recent_products})


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
    if request.method == "POST":
        name = request.POST.get("name", "")
        messages.success(request, f"Спасибо {name}, Ваше сообщение получено.")
        return render(request, "catalog/contacts.html")

    return render(request, "catalog/contacts.html")
