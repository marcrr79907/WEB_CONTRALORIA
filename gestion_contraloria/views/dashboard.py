from ..mixins import IsSuperuserMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, IsSuperuserMixin, TemplateView):

    template_name = 'dashboard.html'
