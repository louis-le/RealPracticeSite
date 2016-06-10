from django.contrib.auth.models import User as BaseUser, UserManager
from django.db import models


class Utility(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "utilities"

class Company(models.Model):


class User(BaseUser):
    company = models.ForeignKey(Company)
    # Use UserManager to get the create_user method, etc.
    objects = UserManager()