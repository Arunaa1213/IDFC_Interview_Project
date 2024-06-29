from django import forms
from .models import RegisterForm

class MyRegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterForm
        fields = ["name","password", "age", "address", "contact", "email"]
