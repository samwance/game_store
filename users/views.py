from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from users.forms import ProfileUserForm, LoginUserForm, RegisterUserForm
from users.models import User


class Login(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {"title": "Authorization"}

    def get_success_url(self):
        return reverse_lazy("store:list")


def logout_user(request):
    logout(request)
    return redirect("users:login")


class Register(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    extra_context = {"title": "Registration"}
    success_url = reverse_lazy("store:list")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(
            phone=form.cleaned_data["phone"], password=form.cleaned_data["password1"]
        )
        if user is not None:
            login(self.request, user)
        return response


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['phone', 'street', 'house_number', 'apartment_number', 'city', 'zip_code', 'photo']
    template_name = "users/profile.html"
    extra_context = {
        "title": "Edit profile",
    }

    def form_valid(self, form):
        form.instance.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy("users:profile")
