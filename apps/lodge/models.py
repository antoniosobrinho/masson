from django.db import models

from apps.common.models import BaseModel
from apps.common.choices import DegreeChoices
from apps.massons.models import Masson


# Create your models here.
class Session(BaseModel):
    date = models.DateField(verbose_name="Data da Sessão")
    degree = models.CharField(
        max_length=50, verbose_name="Grau", choices=DegreeChoices.choices
    )
    presents = models.ManyToManyField(
        Masson, blank=True, related_name="sessions", verbose_name="Presentes"
    )

    def __str__(self):
        return f"Sessão em {self.date} - Grau: {self.degree}"

    class Meta:
        verbose_name = "Sessão"
        verbose_name_plural = "Sessões"
        ordering = ["date"]
