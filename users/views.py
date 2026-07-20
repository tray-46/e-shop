from django.contrib.auth.views import LoginView
from django.core.mail import EmailMessage
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from config.settings import DEFAULT_FROM_EMAIL
from users.forms import RegisterForm, LoginForm


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

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        if email is not None:
            self.send_welcome_email(email)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = LoginForm
