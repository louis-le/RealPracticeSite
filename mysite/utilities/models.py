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

    # Numbers used to keep track of sort order the user left it on.
    ALPHA_SORT = 1
    ALPHA_SORT_I = -1
    LOGIN_SORT = 2
    LOGIN_SORT_I = -2
    JOINED_SORT = 3
    JOINED_SORT_I = -3

    # Alphabetical sorting from A to Z as default.
    utilities_choice_sort = (
        (ALPHA_SORT, "Alphabetically Sorted"),
        (ALPHA_SORT_I, "Alphabetically Sorted Inverted"),
    )
    users_choice_sort = (
        (ALPHA_SORT, "Alphabetically Sorted"),
        (ALPHA_SORT_I, "Alphabetically Sorted Inverted"),
        (LOGIN_SORT, "Login Date Sorted"),
        (LOGIN_SORT_I, "Login Date Sorted Inverted"),
        (JOINED_SORT, "Date Joined Sorted"),
        (JOINED_SORT_I, "Date Joined Sorted Inverted"),
    )
    utilities_sort = models.IntegerField(choices=utilities_choice_sort, default=ALPHA_SORT)
    users_sort = models.IntegerField(choices=users_choice_sort, default=ALPHA_SORT)

    def __str__(self):
        return self.user.get_username()

    def set_manager(self):
        self.manager = not self.manager

    def is_manager(self):
        return self.manager
