from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from users.forms import RegisterForm, LoginForm


# Create your views here.
class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("users:login")


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = LoginForm
