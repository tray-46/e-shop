from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from users.forms import RegisterForm

# Create your views here.
class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("users:login")
