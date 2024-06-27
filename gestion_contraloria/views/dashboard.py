from ..mixins import IsSuperuserMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import *
from datetime import datetime


class DashboardView(LoginRequiredMixin, IsSuperuserMixin, TemplateView):

    template_name = 'dashboard/dashboard.html'

    def get_reports_year_month(self):
        data = []
        try:
            year = datetime.now().year
            for m in range(1, 13):
                reportes = Reporte.objects.filter(fecha__year=year, fecha__month=m).count()
                data.append(reportes)
        except:
            pass
        return data

    def get_orgs(self):
        data = []
        try:
            org_reports = Reporte.objects.all()
            for r in org_reports:
                Organizacion.objects.filter(pk=r.organizacion_id).count()

            data.append(reports)
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reportes_anno_mes'] = self.get_reports_year_month()
        context['auditorias'] = self.get_orgs()
        return context
