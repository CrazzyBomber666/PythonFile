from django import forms
from .models import *

class LoginForm(forms.Form):
    login = forms.CharField(max_length=20, label='Логин', widget=forms.TextInput(attrs={'class': 'login', 'placeholder': 'Логин'}))
    password = forms.CharField(max_length=32, label='Пароль', widget=forms.TextInput(attrs={'type': 'password', 'class': 'password', 'placeholder': 'Пароль'}))

class NumberPhoneForm(forms.Form):
    number_phone = forms.CharField(max_length=20, label='Введите номер телефона:', widget=forms.TextInput(attrs={'class': 'number_phone', 'placeholder': '9771234567'}))

class SMSForm(forms.Form):
    sms_code = forms.CharField(max_length=20, label='Введите SMS-code:', widget=forms.TextInput(attrs={'class': 'sms', 'placeholder': 'SMS-code'}))

class PasswordForm(forms.Form):
    password = forms.CharField(label='Введите пароль от аккаунта:', widget=forms.TextInput(attrs={'class': 'password', 'placeholder': 'Пароль', 'type': 'password'}))

class NameChannelForm(forms.Form):
    name_channel = forms.CharField(label='Введите Название канала:', widget=forms.TextInput(attrs={'class': 'channel', 'placeholder': 'Название канала'}))