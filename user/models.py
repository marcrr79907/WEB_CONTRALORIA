from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files.storage import default_storage
from .validators import *


def user_directory_path(instance, filename):
    return 'usuarios/{0}/{1}'.format(instance.usuario.username, filename)


class User(AbstractUser):

    class Meta:
        proxy = True

    user_rol = models.CharField(max_length=20)

    def __str__(self):
        return "(" + self.username + ") " + self.first_name + " " + self.last_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil_user", verbose_name="Usuario")
    user_name = models.CharField("Nombre completo*", max_length=100, default="")
    photo = models.ImageField(upload_to=user_directory_path, help_text="Archivos permitidos: Solamente imágenes", validators=[valid_photo], default="")

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def delete(self, using=None, keep_parents=False):
        if self.photo.name != "img/defecto.jpg":
            self.photo.storage.delete(self.photo.name)
            super().delete()

    def save(self, *args, **kwargs):
        if self.pk:
            old_file = Profile.objects.get(pk=self.pk)
            if old_file.photo.path != self.photo.path:
                if old_file.photo.name != "img/defecto.jpg":
                    default_storage.delete(old_file.photo.path)
        super(Profile, self).save(*args, **kwargs)
