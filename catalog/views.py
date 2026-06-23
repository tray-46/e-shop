from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from catalog.models import Feedback
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
