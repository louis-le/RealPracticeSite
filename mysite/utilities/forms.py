from django import forms
from django.contrib.auth.models import User
from .models import Utility


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UtilityForm(forms.ModelForm):
    class Meta:
        model = Utility
        fields = ['name', 'description']
