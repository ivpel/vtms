from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Suite


class SuiteForm(forms.Form):
    class Meta:
        model = Suite

        fields = ['name', 'description']


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'id': 'Username', 'type': 'text', 'placeholder': 'User Name'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'id': 'password', 'type': 'password', 'placeholder': 'Password'}
        )
