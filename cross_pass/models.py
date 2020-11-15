from django.db import models

# Create your models here.
class CrossPass(models.Model):
    ovrpsNm = models.CharField(max_length = 100)
    latitude = models.CharField(max_length = 15)
    longitude = models.CharField(max_length = 15)
    rdnmadr = models.CharField(max_length = 100)
    handicapCvntlYn = models.CharField(max_length = 1)
    handicapCvntlType = models.CharField(max_length = 10)
    handicapCvntlCo = models.PositiveIntegerField(default=0)
