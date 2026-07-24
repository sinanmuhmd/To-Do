from django import forms
from .models import td_model


class td_form(forms.Form):
    title= forms.CharField()
class td_modelform(forms.ModelForm):
    class Meta():
        model = td_model
        fields = '__all__'
