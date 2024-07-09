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

    user_group = None


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_queryset(self):
        user = self.request.user

        grupo_gerente = Group.objects.get(name='Gerente')
        grupo_auditor = Group.objects.get(name='Auditor')

        if grupo_gerente in user.groups.all():
            return Reporte.objects.all()

        elif grupo_auditor in user.groups.all():
            return Reporte.objects.filter(user_id=user)

        else:
            return Reporte.objects.none()


    def get_context_data(self, **kwargs):
        if self.request.user.groups.all():
            self.user_group = self.request.user.groups.all()[0]

        context = super().get_context_data(**kwargs)
        context['title_list'] = 'Reporte(s)'
        context['title'] = 'Añadir Reporte'
        context['entity'] = Reporte
        context['user_group'] = self.user_group
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
                print(request.POST)
                if form.is_valid():
                    form.instance.user_id = self.request.user
                    form.instance.user_name = self.request.user.username
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


class ReporteDeleteView(LoginRequiredMixin, ValidatedPermissionRequiredMixin, View):
    model = Reporte
    success_url = reverse_lazy('gestion_contraloria:report_list')
    template_name = 'dashboard/dashboard.html'
    permission_required = 'delete_reporte'

    def post(self, request, *args, **kwargs):
        data = {}
        data['form_is_valid'] = False

        try:
            action = request.POST['action_update']
            if action == 'update':
                report = Reporte.objects.get(pk=int(request.POST['report_id']))

                if report:
                    if report.user_id == request.user:
                        report.user_id = None
                        request.session['data'] = {
                            'success_message': 'El reporte se ha eliminado con éxito.',
                        }
                        print(request.POST['report_id'])
                        report.save()
                        data['form_is_valid'] = True
                else:
                    data['error'] = 'No hay ningún reporte'
            else:
                data['error'] = 'No ha ingresado ninguna acción'
        except Exception as e:
            data['error'] = str(e)
            print(data['error'])

        if data['form_is_valid']:

            return redirect(self.success_url)
        else:
            request.session['data'] = {
                'error_message': data['error']}
            return redirect(self.success_url)
