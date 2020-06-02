from django.db import models
from django.urls import reverse
# Create your models here.


class OdooReport(models.Model):
    model_name = models.CharField("Model Name", max_length=20)

    def get_absolute_url(self):
        return reverse("odoo:odooreport-list")