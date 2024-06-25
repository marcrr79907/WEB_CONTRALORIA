import requests
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from ..models import *
from ..forms import OrganizacionForm

class OrganizacionListView(LoginRequiredMixin, ListView):
    model = Organizacion
    template_name = 'organizacion.html'

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
        is_empty = True if user_organizacion_list.count() == 0 else False
        title = 'Organizaciones' if len(organizacion_list) > 1 else 'Organización'

        context = super().get_context_data(**kwargs)
        context['title_list'] = title
        context['title'] = 'Agregar Organización'
        context['entity'] = Organizacion
        context['object_list'] = organizacion_list
        context['user_object_list'] = organizacion_reportes_list
        context['action'] = 'add'
        context['action_update'] = 'update'
        context['message'] = 'Sin organizaciones para auditar'
        context['is_empty'] = is_empty
        context['data'] = self.request.session.pop('data', None)

        return context


class OrganizacionUpdateView(LoginRequiredMixin, UpdateView):
    model = Organizacion
    form_class = OrganizacionForm
    template_name = 'organizacion.html'
    success_url = reverse_lazy('gestion_contraloria:organization_update')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        data['form_is_valid'] = False

        try:
            action = request.POST['action_update']
            if action == 'update':
                form = self.get_form()
                if form.is_valid():
                    organizacion = Organizacion.objects.get(pk=self.request.POST['organizacion_id'])

                    if organizacion.en_supervision:
                        organizacion.en_supervision = None
                    else:
                        organizacion.en_supervision = self.request.user

                    organizacion.save()
                    form.save()
                    data['form_is_valid'] = True

                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado ninguna acción'
        except Exception as e:
            data['error'] = str(e)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir organización'

        return context

