from django.db import models

class DegreeChoices(models.TextChoices):
    APPRENTICE  = "AM", "Aprendiz"
    FELLOW  = "CM", "Companheiro"
    MASTER  = "MM", "Mestre"
    INSTALLED_MASTER  = "MI", "Mestre Instalado"