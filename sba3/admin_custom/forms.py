from django import forms
from sba3.models import School

class LoginForm(forms.Form):
    label_suffix = ''
    email = forms.EmailField(required=True, label='Email', initial='')
    password = forms.CharField(required=True, label='Password')

class RegisterAdminForm(forms.Form):
    email = forms.EmailField(required=True, label='Email', initial='', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    tmp_password = forms.CharField(required=True, label='Temporary Password', widget=forms.TextInput(attrs={'class': 'form-control'}))
    school = forms.ModelChoiceField(required=True, label='School', queryset=School.objects.all().order_by('name'), widget=forms.Select(attrs={'class': 'form-control'}))
    # password_confirm = forms.CharField(required=True, label='Confirm Password', widget=forms.TextInput(attrs={'class': 'form-control', 'type':'password'}))
    superuser = forms.BooleanField(required=True, label="Global Admin?", widget=forms.CheckboxInput(attrs={'class': ''}))

class RegisterSchoolForm(forms.Form):
    school_name = forms.CharField(required=True, label='Name', initial='', max_length=75, widget=forms.TextInput(attrs={'class': 'form-control'}))
    school_location = forms.CharField(required=False, label='Location', initial='', widget=forms.TextInput(attrs={'class': 'form-control'}))
    survey_title = forms.CharField(required=False, label='Survey Title', initial='', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

class EditGlobalAdminForm(forms.Form):
    email = forms.EmailField(required=True, label='Email', initial='', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # have to explicitly check if user wants password updated as well since it is within same form
    change_password = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'change_password'}))
    password = forms.CharField(required=False, label='New Password', widget=forms.TextInput(attrs={'class': 'form-control', 'type':'password'}))
    confirm_password = forms.CharField(required=False, label='Confirm New Password', widget=forms.TextInput(attrs={'class': 'form-control', 'type':'password'}))

class EditSchoolAdminForm(forms.Form):
    email = forms.EmailField(required=True, label='Email', initial='', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    school = forms.ModelChoiceField(required=True, label='Change School', queryset=School.objects.all().order_by('name'), widget=forms.Select(attrs={'class': 'form-control'}))
    # have to explicitly check if user wants password updated as well since it is within same form
    change_password = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'change_password'}))
    password = forms.CharField(required=False, label='New Password', widget=forms.TextInput(attrs={'class': 'form-control', 'type':'password'}))
    confirm_password = forms.CharField(required=False, label='Confirm New Password', widget=forms.TextInput(attrs={'class': 'form-control', 'type':'password'}))
