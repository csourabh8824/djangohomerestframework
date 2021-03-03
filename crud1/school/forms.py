from django import forms
from .models import Student


class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = '__all__'
