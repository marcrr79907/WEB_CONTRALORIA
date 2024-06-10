from django.urls import path
from . import views

urlpatterns = [	
	path('inicio_login/', views.inicio_login, name="inicio_login"),
    path('iniciar_session/', views.iniciar_session, name='iniciar_session'),
    path('cerrar_session/', views.cerrar_session, name='cerrar_session'),

    path('inicio_login_panel', views.inicio_login_panel, name="inicio_login_panel"),

    path('perfil_personal/', views.perfil_personal, name='perfil_personal'),
    path('editar_perfil_personal/', views.editar_perfil_personal, name="editar_perfil_personal"),
    path('cambiar_contrasenia/', views.cambiar_contrasenia, name="cambiar_contrasenia"),
]
