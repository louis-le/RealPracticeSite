from django.db import models


class Utility(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    users = []

    def __str__(self):
        return self.name
