from django.contrib.auth.forms import UserCreationForm
from django import forms

from polls import models
from polls.models import AdvUser
from polls.utilities import get_timestamp_path


class UserRegisterForm(UserCreationForm):
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = AdvUser
        fields = ('last_name', 'first_name', 'username', 'password1', 'password2', 'photo_file')