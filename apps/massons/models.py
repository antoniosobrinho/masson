from django.db import models


# Create your models here.
class Masson(models.Model):
    name = models.CharField(max_length=100, unique=False, verbose_name="Nome")
    grade = models.CharField(
        max_length=50,
        verbose_name="Grau",
        choices=[
            ("Aprendiz", "Aprendiz"),
            ("Companheiro", "Companheiro"),
            ("Mestre", "Mestre"),
            ("Meste Instalado", "Meste Instalado"),
        ],
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Maçom"
        verbose_name_plural = "Maçons"
        ordering = ["name"]
