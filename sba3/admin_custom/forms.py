from django import forms

class LoginForm(forms.Form):
	label_suffix = ''
	email = forms.EmailField(required=True, label='Email', initial='')
	password = forms.CharField(required=True, label='Password')

class registerSchoolUserForm(forms.Form):
	school_name = forms.CharField(required=True, label='School Name', initial='')
	# school_username = forms.CharField(required=True, label='School Email', initial='')
	# password = forms.CharField(required=True, label='Password')