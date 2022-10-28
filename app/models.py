from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Form(models.Model):
    Title = models.CharField(max_length=225)
    image = models.ImageField(upload_to="Images")