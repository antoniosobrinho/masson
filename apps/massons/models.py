from django.db import models

from apps.common.models import BaseModel
from apps.common.choices import DegreeChoices


# Create your models here.
class Masson(BaseModel):
    name = models.CharField(max_length=100, unique=False, verbose_name="Nome")
    degree = models.CharField(
        max_length=50,
        verbose_name="Grau",
        choices=DegreeChoices.choices,
        default=DegreeChoices.APPRENTICE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Maçom"
        verbose_name_plural = "Maçons"
        ordering = ["name"]
