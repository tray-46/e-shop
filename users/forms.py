from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control",})

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].label = "Пароль"
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control", })
