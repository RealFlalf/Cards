from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Card, CardPost

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя:', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label='Пароль:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль:', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя:', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Пароль:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CreateCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['first_name', 'last_name', 'birthday', 'photo']
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'birthday': forms.DateInput(format='%m/%d/%Y'),
            'photo': forms.FileInput(),
        }


class CreateCardPostForm(forms.ModelForm):
    class Meta:
        model = CardPost
        fields = ['content', 'photo',]
        widgets = {
            'content': forms.TextInput(),
            'photo': forms.FileInput(),
        }
