from django import forms
from .models import StudentModel


class Loginform(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['username', 'password']
        widgets = {"password": forms.PasswordInput(),
                   "username": forms.TextInput()}
