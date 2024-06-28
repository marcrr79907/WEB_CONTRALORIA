from django.urls import path
from .views.dashboard import DashboardView
from .views.organizacion_views import *
from .views.reporte_views import ReporteListView, ReporteCreateView, ReporteUpdateView, ReporteDeleteView

app_name = 'gestion_contraloria'
urlpatterns = [
    ##################################### dashboard #####################################
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    ##################################### organization #####################################
    path('organization_list/', OrganizacionListView.as_view(), name='organization_list'),
    path('organization_update/', OrganizacionUpdateView.as_view(), name='organization_update'),

    ##################################### report #####################################
    path('report_list/', ReporteListView.as_view(), name='report_list'),
    path('report_create/', ReporteCreateView.as_view(), name='report_create'),
    path('report_update/<int:pk>/', ReporteUpdateView.as_view(), name='report_update'),
    path('report_delete/<int:pk>/', ReporteDeleteView.as_view(), name='report_delete'),
]