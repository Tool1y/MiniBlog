from django import forms
from .models import Comments
from django.contrib.auth.forms import UserCreationForm


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', min_length=5, max_length=150)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Потвердить пароль', widget=forms.PasswordInput)


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'text_comments')
