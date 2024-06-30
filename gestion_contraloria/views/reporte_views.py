import requests
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, View, CreateView, DeleteView
from ..mixins import IsSuperuserMixin, ValidatedPermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import *
from ..forms import ReportForm


class ReporteListView(LoginRequiredMixin, ValidatedPermissionRequiredMixin, ListView):
    model = Reporte
    template_name = 'dashboard/dashboard.html'
    permission_required = 'view_reporte'
    context_object_name = 'user_report_list'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_queryset(self):
        user = self.request.user
        grupo_gerente = Group.objects.get(name='Gerente')
        grupo_auditor = Group.objects.get(name='Auditor')

        if grupo_gerente in user.groups.all():
            # Gerente, puede ver todos los reportes de Auditores
            return Reporte.objects.filter(user_id__groups=grupo_auditor)
        elif grupo_auditor in user.groups.all():
            # Auditor, solo puede ver sus propios reportes
            return Reporte.objects.filter(user_id=user)
        else:
            # Manejar otros grupos o usuarios que no pertenecen a Gerente ni Auditor
            return Reporte.objects.none()




    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['title_list'] = 'Reporte(s)'
        context['title'] = 'Añadir Reporte'
        context['entity'] = Reporte
        context['action_add'] = 'add'
        context['action_update'] = 'update'
        context['message'] = 'No se ha creado ningún reporte'
        context['data'] = self.request.session.pop('data', None)

        return context


class ReporteCreateView(LoginRequiredMixin, ValidatedPermissionRequiredMixin, CreateView):
    model = Reporte
    template_name = 'dashboard/dashboard.html'
    permission_required = 'add_reporte'
    form_class = ReportForm
    success_url = reverse_lazy('gestion_contraloria:report_list')

    def post(self, request, *args, **kwargs):
        data = {}
        data['form_is_valid'] = False
        try:
            action = request.POST['action_add']
            if action == 'add':
                form = self.get_form()

                if form.is_valid():
                    form.instance.user_id = self.request.user
                    form.save()
                    data['form_is_valid'] = True
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado ninguna acción!'

        except Exception as e:
            data['error'] = str(e)

        if data['form_is_valid']:
            request.session['data'] = {
                'success_message': 'El reporte ha sido creado con éxito.'}
            return redirect(self.success_url)
        else:
            request.session['data'] = {
                'error_message': data['error']}
            return redirect(self.success_url)


class ReporteUpdateView(LoginRequiredMixin, ValidatedPermissionRequiredMixin, UpdateView):
    model = Reporte
    template_name = 'dashboard/dashboard.html'
    permission_required = 'change_reporte'
    form_class = ReportForm
    success_url = reverse_lazy('gestion_contraloria:report_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        data['form_is_valid'] = False

        try:
            action = request.POST['action_update']
            print(request.POST)
            if action == 'update':
                form = self.get_form()
                if form.is_valid():
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
                'success_message': 'El reporte ha sido actualizado con éxito.'}
            return redirect(self.success_url)
        else:
            request.session['data'] = {
                'error_message': data['error']}
            return redirect(self.success_url)


class ReporteDeleteView(LoginRequiredMixin, ValidatedPermissionRequiredMixin, DeleteView):
    model = Reporte
    success_url = reverse_lazy('gestion_contraloria:report_list')
    template_name = 'reporte/eliminar.html'
    permission_required = 'delete_reporte'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar reporte'
        context['text'] = 'Está seguro de eliminar el reporte?'
        context['url_redirect'] = self.success_url

        return context

