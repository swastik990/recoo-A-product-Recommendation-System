from django.contrib import admin
from . import models
# Register your models here.

register_model = models.Products

admin.site.register(register_model)