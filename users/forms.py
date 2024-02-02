from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)

from django import forms
from users.models import User


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class LoginUserForm(StyleMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = ["password"]


class RegisterUserForm(StyleMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "phone", "password1", "password2"]

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError("This phone already exists")
        return phone


class ProfileUserForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ["phone", "username", "photo"]
        labels = {
            "phone": "Phone",
            "username": "Name",
            "photo": "Photo",
        }
        widgets = {
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "photo": forms.FileInput(attrs={"class": "form-select-image"}),
        }
