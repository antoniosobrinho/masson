from django.db import models

from apps.common.manager import ActiveBaseEntityManager

# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, null=True)

    active = ActiveBaseEntityManager()
