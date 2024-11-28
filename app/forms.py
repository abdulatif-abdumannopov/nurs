from .models import *
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'class': 'form_field',
        'placeholder': 'Имя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form_field',
        'placeholder': 'Пароль'
    }))
class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'text']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form_field_feedback',
                'placeholder': 'Имя',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form_field_feedback',
                'placeholder': 'Email',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form_text_field',
                'placeholder': 'Текст',
            })
        }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form_field', 'placeholder': 'Email'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form_field', 'placeholder': 'Имя'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form_field', 'placeholder': 'Пароль'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form_field', 'placeholder': 'Повторите Пароль'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким Email уже существует.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким Username уже существует.")
        return username