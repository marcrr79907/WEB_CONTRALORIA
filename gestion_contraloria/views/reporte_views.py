import requests
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, View, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from ..models import *
from ..forms import ReportForm


class ReporteListView(LoginRequiredMixin, ListView):
    model = Reporte
    template_name = 'dashboard/dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        user_report_list = Reporte.objects.filter(
            user_id=self.request.user
        )
        reportes = Reporte.objects.filter()

        context = super().get_context_data(**kwargs)
        context['title_list'] = 'Reporte(s)'
        context['title'] = 'Añadir Reporte'
        context['entity'] = Reporte
        context['user_report_list'] = user_report_list
        context['reportes'] = reportes
        context['action_add'] = 'add'
        context['action_update'] = 'update'
        context['message'] = 'No se ha creado ningún reporte'
        context['data'] = self.request.session.pop('data', None)

        return context


class ReporteCreateView(LoginRequiredMixin, CreateView):
    model = Reporte
    template_name = 'dashboard/dashboard.html'
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


class ReporteUpdateView(LoginRequiredMixin, UpdateView):
    model = Reporte
    template_name = 'dashboard/dashboard.html'
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


class ReporteDeleteView(LoginRequiredMixin, DeleteView):
    model = Reporte
    success_url = reverse_lazy('gestion_contraloria:report_list')
    template_name = 'reporte/eliminar.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar reporte'
        context['text'] = 'Está seguro de eliminar el reporte?'
        context['url_redirect'] = self.success_url

        return context

