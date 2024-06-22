from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import Userperfil
from .forms import UserUpdateForm
from django.views.generic.edit import UpdateView, FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from core import settings


class UsersLoginView(LoginView):
    template_name = 'login.html'

  
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = Userperfil
    form_class = UserUpdateForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('user:profile')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        data = {}

        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                if form.is_valid():
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
        context = super().get_context_data(**kwargs)

        context['user'] = user

        return context   

class SegurityUserView(LoginRequiredMixin, FormView):

    model = Userperfil
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
