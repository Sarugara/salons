from django.contrib.auth.models import User
from django import forms
from .models import Salons


class SalonsForm(forms.ModelForm):
    class Meta:
        model = Salons
        fields = ['name', 'salon_desc', 'salon_adress', 'salon_logo']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']