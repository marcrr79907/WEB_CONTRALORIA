from django.contrib import messages
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from crum import get_current_request
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy


class IsSuperuserMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/admin/')


class AuditorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        es_auditor = self.request.user.groups.filter(name='Auditor').exists()
        es_gerente = self.request.user.groups.filter(name='Gerente').exists()
        has_perms = es_auditor or es_gerente

        return has_perms

    def handle_no_permission(self):
        messages.error(self.request, 'No tiene permisos para acceder a este módulo.')
        return redirect('gestion_contraloria:dashboard')

class GerenteRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Gerente').exists()

    def handle_no_permission(self):
        messages.error(self.request, 'No tiene permisos para acceder a este módulo.')
        return redirect('gestion_contraloria:dashboard')


class ValidatedPermissionRequiredMixin(object):

    permission_required = ''
    url_redirect = None

    def get_perms(self):
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required
        print(perms)
        return perms

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('gestion_contraloria:dashboard')
        return self.url_redirect
    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)

        messages.error(request, 'No tiene permisos para acceder a este módulo.')
        return HttpResponseRedirect(self.get_url_redirect())
