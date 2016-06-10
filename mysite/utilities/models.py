from django.contrib.auth.models import User
from django.db import models


class Utility(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "utilities"
