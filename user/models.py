from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.db.models.signals import post_save
from .validators import *

# Create your models here.
def user_directory_path(instance, filename):
    return 'usuarios/{0}/{1}'.format(instance.usuario.username, filename)

class Userperfil(User):
    class Meta:
        proxy = True

    user_rol = models.TextChoices()

    def __str__(self):
        return "(" + self.username + ") " + self.first_name + " " + self.last_name

class Perfil(models.Model):
    usuario = models.OneToOneField(Userperfil, on_delete=models.CASCADE, related_name="perfil_user", verbose_name="Usuario")
    nombre_user = models.CharField("Nombre completo*", max_length=100, default="")
    foto = models.ImageField(upload_to=user_directory_path, help_text="Archivos permitidos: Solamente imágenes", validators=[valid_foto], default="")

    def __str__(self):
        return self.usuario.username
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def delete(self, using=None, keep_parents=False):
        if self.foto.name != "img/defecto.jpg":
            self.foto.storage.delete(self.foto.name)
            super().delete()

    def save(self, *args, **kwargs):
        if self.pk:
            old_file = Perfil.objects.get(pk=self.pk)
            if old_file.foto.path != self.foto.path:
                if old_file.foto.name != "img/defecto.jpg":
                    default_storage.delete(old_file.foto.path)
        super(Perfil, self).save(*args, **kwargs)