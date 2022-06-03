from django import forms
from django.conf import settings

from movies.models import Movie
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.forms import ValidationError



class CreateMoviesForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = 'title descriptions director'.split()

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название!',
                    'rows': 10
                }
            ),
            'descriptions': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание'
                }
            ),
            'director': forms.Select(
                attrs={
                    'class': 'form-control form-control-custom',

                }
            )
        }

class LoginForms(forms.Form):
    username = forms.CharField(label='Имя пользователя',widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter username',
            'rows': 10
        }
    ))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        }
    ))




class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='150 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Потверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='g-Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




# class RegisterForm(forms.Form):
#     username = forms.CharField(label='Логин', widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter username'
#         }
#     ))
#     password = forms.CharField(label='Пароль',widget=forms.PasswordInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter password',
#
#         }
#     ))
#     password2 = forms.CharField(label='Пароль еще раз',widget=forms.PasswordInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Repeat password'
#         }
#     ))
#
#
#     # def clean_title(self):
#     #     title = self.cleaned_data['username']
#     #     if len(title) > 200:
#     #         raise ValidationError('Длина превышает 200 символов')
#     #     return username
#     #
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if User.objects.filter(username=username).count()>0:
#             raise ValidationError('USER WITH THIS USERNAME ALREADY EXISTS')
#         return username
#
#     def save(self):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         user = User.objects.create_user(username=username, password=password)
#         return user
#
#     def clean_pass(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("НЕВЕРНЫЙ ПАРОЛЬ")
#         return password2

# def clean_pass(self):
#     cleaned_data = super(RegisterForm, self).clean()
#
#     password = cleaned_data.get('password')
#     password_confirm = cleaned_data.get('password_confirm ')
#
#     if password and password_confirm:
#         if password != password_confirm:
#             raise forms.ValidationError("The two password fields must match.")
#     return cleaned_data
#
