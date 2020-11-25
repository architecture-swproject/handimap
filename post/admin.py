from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Photo)
admin.site.register(models.Review)
admin.site.register(models.Star)
admin.site.register(models.Carrier)