from django import forms

class LoginForm(forms.Form):
	error_css_class = "error"
	required_css_class = "required"
	label_suffix = ""

	email = forms.EmailField(required=True, label="Email")
	password = forms.CharField(required=True, label="Password")