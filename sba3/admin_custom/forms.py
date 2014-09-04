from django import forms

from sba3.models import School

class LoginForm(forms.Form):
    label_suffix = ''
    email = forms.EmailField(required=True, label='Email', initial='')
    password = forms.CharField(required=True, label='Password')

class registerAdminForm(forms.Form):
    # school_name = forms.CharField(required=True, label='School Name', initial='')
    email = forms.EmailField(required=True, label='Email', initial='', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, label='Password', widget=forms.TextInput(attrs={'class': 'form-control', 'type':'password'}))
    password_confirm = forms.CharField(required=True, label='Confirm Password', widget=forms.TextInput(attrs={'class': 'form-control', 'type':'password'}))

    superuser = forms.BooleanField(required=False, label="Global Admin?", widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    school = forms.ModelChoiceField(required=False, label='School', queryset=School.objects.all().order_by('name'), widget=forms.Select(attrs={'class': 'form-control'}))

class registerSchoolUserForm(forms.Form):
	school_name = forms.CharField(required=True, label='School Name', initial='')
	# school_username = forms.CharField(required=True, label='School Email', initial='')
	# password = forms.CharField(required=True, label='Password')
