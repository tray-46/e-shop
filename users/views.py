from typing import Optional

from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.core.mail import EmailMessage
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from config.settings import DEFAULT_FROM_EMAIL
from users.forms import LoginForm, RegisterForm, UserProfileForm
from users.models import User


# Create your views here.
class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("users:login")

    @staticmethod
    def send_welcome_email(email_address: str) -> None:
        """Send a welcome email to the email address"""
        mail_subject = "Welcome to our community"
        message = "Thank you for registering."
        recipient_list = [email_address]
        email = EmailMessage(mail_subject, message, DEFAULT_FROM_EMAIL, to=recipient_list)
        email.send()

    def form_valid(self, form: RegisterForm) -> HttpResponse:
        email = form.cleaned_data.get("email")
        if email is not None:
            self.send_welcome_email(email)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = LoginForm


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset: Optional[QuerySet[User]] = None) -> User:
        user = get_object_or_404(User, pk=self.request.user.pk)
        return user

    def form_valid(self, form: UserProfileForm) -> HttpResponse:
        form.save()
        success_message = "Изменения сохранены."
        messages.success(self.request, success_message)
        return super().form_valid(form)
