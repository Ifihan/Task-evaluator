from django import forms
from .models import Company, Information


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'


class InformationForm(forms.ModelForm):

    class Meta:
        model = Information
        fields = '__all__'
