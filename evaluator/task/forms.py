from django import forms
from .models import Companie, Information


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Companie
        fields = '__all__'


class InformationForm(forms.ModelForm):

    class Meta:
        model = Information
        fields = '__all__'
