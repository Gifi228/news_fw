from django import forms
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, \
                                        UserCreationForm

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'description',
            'photo',
            'category'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок статьи'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Содержание статьи'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            })
        }



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя",
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username'
                               }))



    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                    'placeholder': 'Password'
                               }))


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя",
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username'
                               }))

    first_name = forms.CharField(label="Ваше Имя",
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'First name'
                               }))

    last_name = forms.CharField(label="Ваша Фамилия",
                                 widget=forms.PasswordInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Last name'
                                 }))

    email_name = forms.CharField(label="Ваша почта",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Your email'
                                }))

    password1 = forms.CharField(label="Придумайте пароль",
                                 widget=forms.PasswordInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Password'
                                 }))

    password2 = forms.CharField(label="Подтвердите пароль",
                                 widget=forms.PasswordInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Password'
                                 }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')