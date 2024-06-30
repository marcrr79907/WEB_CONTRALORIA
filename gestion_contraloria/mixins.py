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



class ValidatedPermissionRequiredMixin(object):

    permission_required = ''
    url_redirect = None


    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('gestion_contraloria:dashboard')
        return self.url_redirect


    def get_perms(self):
        perms = []
        if isinstance(self.permission_required, str):
            perms.append(self.permission_required)
        else:
            perms = list(self.permission_required)
        print(perms)
        return perms

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        user_group = request.user.groups.all()[0]
        print(user_group)
        perms = self.get_perms()
        if user_group:
            for p in perms:
                if not user_group.permissions.filter(codename=p).exists():
                    messages.error(request, 'No tiene permisos para este modulo.')
                    return HttpResponseRedirect(self.get_url_redirect())
            return super().dispatch(request, *args, **kwargs)

        messages.error(request, 'No tiene permisos para este modulo.')
        return HttpResponseRedirect(self.get_url_redirect())

