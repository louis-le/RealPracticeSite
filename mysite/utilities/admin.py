from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Utility, Company, Employee


class EmployeeInline(admin.StackedInline):
    model = Employee
    filter_horizontal = ('utilities',)


class UserAdmin(UserAdmin):
    inlines = [EmployeeInline, ]


class CompanyAdmin(admin.ModelAdmin):
    model = Utility
    inlines = [EmployeeInline, ]
    filter_horizontal = ('utilities',)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Utility)
admin.site.register(Company, CompanyAdmin)
