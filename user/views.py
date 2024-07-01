from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import UserUpdateForm
from django.views.generic.edit import UpdateView, FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from core import settings


class UsersLoginView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        user = request.user

        if user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)

        return super().dispatch(request, *args, **kwargs)

