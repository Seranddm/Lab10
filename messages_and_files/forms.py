from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import *


class CreateMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'msg_file', 'recipient']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        message = super().save(commit=False)
        # связываю автора с сообщением
        message.sender = self.user
        if message.msg_file:
            message.file_name = message.msg_file.name
        if commit:
            message.save()
        return message


class UserLoginForm(AuthenticationForm):
    # Форма аутентификации
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
