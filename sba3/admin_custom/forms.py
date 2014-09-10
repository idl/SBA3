from django import forms

from sba3.models import School

class LoginForm(forms.Form):
    label_suffix = ''
    email = forms.EmailField(required=True, label='Email', initial='')
    password = forms.CharField(required=True, label='Password')

class registerAdminForm(forms.Form):
    email = forms.EmailField(required=True, label='Email', initial='', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, label='Password', widget=forms.TextInput(attrs={'class': 'form-control', 'type':'password'}))
    password_confirm = forms.CharField(required=True, label='Confirm Password', widget=forms.TextInput(attrs={'class': 'form-control', 'type':'password'}))
    school = forms.ModelChoiceField(required=True, label='School', queryset=School.objects.all().order_by('name'), widget=forms.Select(attrs={'class': 'form-control'}))
    superuser = forms.BooleanField(required=True, label="Global Admin?", widget=forms.CheckboxInput(attrs={'class': ''}))

class registerSchoolUserForm(forms.Form):
	school_name = forms.CharField(required=True, label='School Name', initial='')
	# password = forms.CharField(required=True, label='Password')
