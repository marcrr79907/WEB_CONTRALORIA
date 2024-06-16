from django.urls import path
from .views.dashboard import DashboardView

app_name = 'gestion_contraloria'
urlpatterns = [
    ########## dashboard #############
    path('dashboard/' ,DashboardView.as_view(), name='dashboard')
]