from django.db import models
from django.core.files.storage import default_storage
from django.db.models.signals import post_save
from .validators import *

# Create your models here.