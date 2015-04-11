from django import forms

from ..models import School

class surveyLoginForm(forms.Form):
    school_list = School.objects.all().order_by('name')

    school = forms.ModelChoiceField(required=False, label='School', queryset=school_list, widget=forms.Select(attrs={'class': 'form-control'}))
    identifier = forms.CharField(required=True, label='Identifier', widget=forms.TextInput(attrs={'class': 'form-control'}))

class surveyContinueForm(forms.Form):
    school_list = School.objects.all().order_by('name')
    
    school = forms.ModelChoiceField(required=False, label='School', queryset=school_list, widget=forms.Select(attrs={'class': 'form-control'}))
    identifier = forms.CharField(required=True, label='Identifier', widget=forms.TextInput(attrs={'class': 'form-control'}))
    passkey = forms.CharField(required=True, label='Passkey', widget=forms.TextInput(attrs={'class': 'form-control'}))