from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Reporte
from datetime import datetime

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return redirect('/admin/')
        user = request.user
        if user.groups.all() and str(user.groups.all()[0]) == 'Auditor':
            return redirect('gestion_contraloria:organization_list')
        return super().dispatch(request, *args, **kwargs)

    def get_reports_year_month(self, year):
        data = []
        try:
            for m in range(1, 12):
                reportes = Reporte.objects.filter(fecha__year=year, fecha__month=m).count()
                data.append(reportes)
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = self.request.GET.get('year', datetime.now().year)

        context['selected_year'] = int(year)
        context['reportes_anno_mes'] = self.get_reports_year_month(year)
        context['years'] = range(datetime.now().year - 5, datetime.now().year + 1)
        return context
