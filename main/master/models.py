from django.db import models

# Create your models here.
class Pasien(models.Model):
    nama = models.CharField(max_length=50)
    umur = models.IntegerField(max_length=2)