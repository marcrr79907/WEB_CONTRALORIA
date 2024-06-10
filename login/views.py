from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import *
from .forms import *
import os
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from core.settings import *
from gestion_contraloria.views import *
from .lenguaje import *
#-------------------------------------------------------------------------------------
# Create your views here.
#-------------------------------------------------------------------------------------
def inicio_login(request):
    if request.user.is_authenticated:
        return redirect('inicio_login_panel')
    else:
        context = {
            'titulo' : titulo_pagina,
            'titulo_sistema' : titulo_sistema,
            'info_user' : submensaje_entrada,
        }
        return render(request, "login.html", context)
#-------------------------------------------------------------------------------------
def iniciar_session(request):
    context = {
        'titulo' : titulo_pagina,
        'titulo_sistema' : titulo_sistema,
        'info_user' : submensaje_entrada,
        'form': AuthenticationForm,
        'error': error_entrada
    }
    if request.method == 'GET':
        return render(request, 'login.html', context)
    else:
        usuario = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=usuario, password=password)
        if user is None:
            return render(request, 'login.html', context)
        else:
            login(request, user)
            url_user = "usuarios/" + request.user.username + "/"
            usuario_dir_final = MEDIA_ROOT + url_user
            os.makedirs(usuario_dir_final, exist_ok=True)
            return redirect('inicio_login_panel')
#-------------------------------------------------------------------------------------
@login_required(login_url='inicio_login')
def inicio_login_panel(request):
    context = {
        'titulo' : titulo_sistema,
        'mensaje_bienvenida' : mensaje_bienvenida,
        'texto_informativo' : texto_informativo,
        'titulo_estadisticas' : titulo_estadisticas,
    }
    return render(request, "plantilla/inicio_login_panel.html", context)
#-------------------------------------------------------------------------------------
@login_required(login_url='inicio_login')
def cerrar_session(request):
    logout(request)
    return redirect('inicio_login')
#-------------------------------------------------------------------------------------
@login_required(login_url='inicio_login')
def perfil_personal(request):
    perfil = Perfil.objects.filter(usuario=request.user)
    if perfil:
        perfil1 = request.user.perfil_user
        context = {
            'titulo' : titulo_perfil,
            'perfil' : perfil1
        }
        return render(request, "perfil_personal.html", context)
    else:
        return crear_perfil_personal(request)
#-------------------------------------------------------------------------------------
@login_required(login_url='inicio_login')
def crear_perfil_personal(request):
    plantilla = 'crear_perfil_personal.html'
    if request.method == 'GET':
        initial_data = {
            'nombre_user': request.user.first_name + " " + request.user.last_name
        }
        context = {
            'titulo' : actualizar_perfil,
            'form': PerfilForm (initial=initial_data)
        }
        return render(request, plantilla , context)
    else:
        try:
            form = PerfilForm(request.POST, request.FILES)
            crear_datos_perfil = form.save(commit=False)
            crear_datos_perfil.usuario = request.user
            crear_datos_perfil.save()
            return redirect('perfil_personal')
        except ValueError:
            context = {
                'titulo' : actualizar_perfil,
                'form': PerfilForm(request.POST, request.FILES),
                'error': mensaje_form_value_error
            }
            return render(request, plantilla, context)
#-------------------------------------------------------------------------------------
@login_required(login_url='inicio_login')
def editar_perfil_personal(request):
    datos_perfil = request.user.perfil_user
    plantilla = 'editar_perfil_personal.html'
    if request.method == 'GET':
        form = PerfilForm(instance=datos_perfil)
        context = {
            'titulo' : actualizar_perfil,
            'datos' : datos_perfil,
            'form': form
        }
        return render(request, plantilla, context)
    else:
        try:
            form = PerfilForm(request.POST, request.FILES, instance=datos_perfil)
            editar_datos_perfil = form.save(commit=False)
            editar_datos_perfil.save()
            return redirect('perfil_personal')
        except ValueError:
            context = {
                'titulo' : actualizar_perfil,
                'datos' : datos_perfil,
                'form': form,
                'error': mensaje_form_value_error
            }
            return render(request, plantilla, context)
#-------------------------------------------------------------------------------------
@login_required(login_url='inicio_login')
def cambiar_contrasenia(request):
    plantilla = 'cambiar_contrasenia.html'
    if request.method == 'GET':
        context = {
            'titulo' : titulo_cambiar_contrasenia,
        }
        return render(request, plantilla, context)
    else:
        actual = request.POST['actual']
        contrasenia = request.POST['password']
        user = User.objects.get(username=request.user.username)
        verificar = user.check_password(actual)
        if verificar:
            user.set_password(contrasenia)
            user.save()
            context = {
                'titulo' : titulo_cambiar_contrasenia,
                'msg' : mensaje_cambio_exito,
            }
            return render(request, plantilla, context)
        else:
            context = {
                'titulo' : titulo_cambiar_contrasenia,
                'msg' : mensaje_cambio_error,
            }
            return render(request, plantilla, context)
#-------------------------------------------------------------------------------------
