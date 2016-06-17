from django.contrib.auth.models import User
from django.db import models


class Utility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "utilities"


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    utilities = models.ManyToManyField(Utility, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "companies"


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    utilities = models.ManyToManyField(Utility, blank=True)
    manager = models.BooleanField()

    def __str__(self):
        return self.user.get_username()

    def set_manager(self):
        self.manager = not self.manager
