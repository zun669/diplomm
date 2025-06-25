from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")

class PatientSearchForm(forms.Form):
            full_name = forms.CharField(
        label="Поиск пациента",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Введите ФИО пациента'})
    )