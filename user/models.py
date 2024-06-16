from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files.storage import default_storage
from .validators import valid_foto


def user_directory_path(instance, filename):
    return 'usuarios/{0}/{1}'.format(instance.usuario.username, filename)


class User(AbstractUser):

    user_rol = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=user_directory_path, help_text="Archivos permitidos: Solamente imágenes", validators=[valid_foto], default="")

    def __str__(self):
        return "(" + self.username + ") " + self.first_name + " " + self.last_name

    def delete(self, using=None, keep_parents=False):
        if self.photo.name != "img/defecto.jpg":
            self.photo.storage.delete(self.photo.name)
            super().delete()

    def save(self, *args, **kwargs):
        if self.pk:
            old_file = User.objects.get(pk=self.pk)
            if old_file.photo.path != self.photo.path:
                if old_file.photo.name != "img/defecto.jpg":
                    default_storage.delete(old_file.photo.path)
        super(User, self).save(*args, **kwargs)

