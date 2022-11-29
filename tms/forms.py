from django import forms
from .models import Suite


class SuiteForm(forms.Form):

    class Meta:
        model = Suite

        fields = ['name', 'description']
