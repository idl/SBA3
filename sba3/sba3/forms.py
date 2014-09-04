from django import forms

from models import School

class surveyLoginForm(forms.Form):
    school = forms.ModelChoiceField(required=True, label='School', queryset=School.objects.all().order_by('name'))
    identifier = forms.CharField(required=True, label='Identifier')