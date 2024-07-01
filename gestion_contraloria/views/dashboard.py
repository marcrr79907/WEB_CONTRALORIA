from django.shortcuts import redirect

from ..mixins import IsSuperuserMixin
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import *
from datetime import datetime


class DashboardView(LoginRequiredMixin, IsSuperuserMixin, TemplateView):

    template_name = 'dashboard/dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return redirect('/admin/')
        user = request.user
        print(type(user.groups.all()[0]))
        if user.groups.all():
            if str(user.groups.all()[0]) == 'Auditor':

                return redirect('gestion_contraloria:organization_list')

        return super().dispatch(request, *args, **kwargs)

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

    def get_context_data(self, **kwargs):


        context = super().get_context_data(**kwargs)
        context['reportes_anno_mes'] = self.get_reports_year_month()
        return context
