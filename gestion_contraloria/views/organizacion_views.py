from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from ..mixins import IsSuperuserMixin, ValidatedPermissionRequiredMixin
from ..models import *

class OrganizacionListView(LoginRequiredMixin, ListView):
    model = Organizacion
    template_name = 'dashboard/dashboard.html'
    # permission_required = 'organizacion.view_organizacion'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        organizacion_list = Organizacion.objects.filter(
            en_supervision=None
        )
        user_organizacion_list = Organizacion.objects.filter(
            en_supervision=self.request.user
        )
        organizacion_reportes_list = [
            [organizacion, Reporte.objects.filter(organizacion_id=organizacion.pk).count()]
            for organizacion in user_organizacion_list
        ]
        title = 'Organizaciones' if len(user_organizacion_list) > 1 else 'Organización'

        context = super().get_context_data(**kwargs)
        context['title_list'] = title
        context['title'] = 'Añadir Organización'
        context['entity'] = Organizacion
        context['organizacion_list'] = organizacion_list
        context['user_organizacion_list'] = organizacion_reportes_list
        context['action_add'] = 'add'
        context['action_update'] = 'update'
        context['message'] = 'Sin organizaciones para auditar'
        context['data'] = self.request.session.pop('data', None)

        return context


class OrganizacionUpdateView(LoginRequiredMixin, View):
    model = Organizacion
    template_name = 'dashboard/dashboard.html'
    # permission_required = 'organizacion.change_organizacion'
    success_url = reverse_lazy('gestion_contraloria:organization_list')
    url_redirect = success_url

    def post(self, request, *args, **kwargs):
        data = {}
        data['form_is_valid'] = False

        try:
            action = request.POST['action_update']
            if action == 'update':
                organizacion = Organizacion.objects.get(pk=int(self.request.POST['id']))

                if organizacion:
                    if organizacion.en_supervision:
                        organizacion.en_supervision = None
                    else:
                        organizacion.en_supervision = self.request.user

                    organizacion.save()
                    data['form_is_valid'] = True
                else:
                    data['error'] = 'No hay ninguna organización'
            else:
                data['error'] = 'No ha ingresado ninguna acción'
        except Exception as e:
            data['error'] = str(e)
            print(data['error'])

        if data['form_is_valid']:
            request.session['data'] = {
                'success_message': 'La organización se ha añadido con éxito.',
                'delete_message': 'La organización se ha eliminado con éxito.',
            }
            return redirect(self.success_url)
        else:
            request.session['data'] = {
                'error_message': data['error']}
            return redirect(self.success_url)
