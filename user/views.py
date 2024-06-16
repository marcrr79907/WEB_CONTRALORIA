from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import User
from .forms import CustomUserCreationForm, UserUpdateForm
from django.views.generic.edit import UpdateView, FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from core import settings


class UsersLoginView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ingrese usuario y contraseña'
        return context
  
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'editp.html'
    success_url = reverse_lazy('users:profile')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        data = {}

        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                phone = Phone_DB.objects.get(number=request.POST['phone'])
                if form.is_valid():
                    if phone:
                        form.save()

                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado ninguna acción'
        except Exception as e:
            data['error'] = str(e)

        return redirect(self.success_url) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar usuario'
        context['url_redirect'] = self.success_url
        context['action'] = 'edit'

        return context   

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        data_user = Person_DB.objects.get(dni=user.ci)
        context = super().get_context_data(**kwargs)

        context['data_user'] = data_user
        context['user'] = user

        return context   

class SegurityUserView(LoginRequiredMixin, FormView):

    model = User
    form_class = PasswordChangeForm
    template_name = 'segurity.html'
    url_redirect = reverse_lazy('users:segurity')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = PasswordChangeForm(user=self.request.user)
        return form

    def post(self, request, *args, **kwargs):

        data = {}
        data['form_is_valid'] = False

        try:
            action = request.POST['action']
            if action == 'edit':
                form = PasswordChangeForm(user=request.user, data=request.POST)
                if form.is_valid():

                    data['form_is_valid'] = True
                    form.save()
                    update_session_auth_hash(request, form.user)
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado ninguna acción'
        except Exception as e:
            data['error'] = str(e)

        if data['form_is_valid']:
            request.session['data'] = {
                'success_message': 'La contraseña ha sido actualizada con éxito.'}
            return redirect(self.url_redirect)
        else:
            request.session['data'] = {
                'error_message': data['error']}
            return redirect(self.url_redirect)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cambiar contraseña'
        context['url_redirect'] = self.success_url
        context['data'] = self.request.session.pop('data', None)
        context['action'] = 'edit'

        return context
