from django import forms
from .models import Student
# If you are using model name in createview then use this
# class RegistrationForm(forms.Form):
#     name = forms.CharField(max_length=20)
#     email = forms.EmailField()


# If you are using form class in createview then use this
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email"]
