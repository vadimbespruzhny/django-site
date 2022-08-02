from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25, label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=20, label='Пароль', widget=forms.TextInput(
        attrs={'class': 'form-control'}))


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=25, label='Имя', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=50, label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=25, label='Пароль', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=20, label='Подтверждение пароля', widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password_2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('password dont match')
        return cd['password2']


class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class PasswordChangeForm(forms.Form):
    old_pwd = forms.CharField(
        label='Введите старый пароль', max_length=25, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    new_pwd1 = forms.CharField(
        label='Введите новый пароль', max_length=25, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    new_pwd2 = forms.CharField(
        label='Введите новый пароль еще раз', max_length=25, widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    def clean_password(self):
        new_pwd1 = self.cleaned_data.get('new_pwd1')
        new_pwd2 = self.cleaned_data.get('new_pwd2')
        if new_pwd1 != new_pwd2:
            raise ValidationError('password dont match')
        return new_pwd2
