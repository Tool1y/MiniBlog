from django import forms
from django.contrib.auth.models import User

from .models import Comments
from django.contrib.auth.forms import UserCreationForm


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", min_length=5, max_length=150)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Потверждение пароля', widget=forms.PasswordInput)

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'text_comments')
