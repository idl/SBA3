from django import forms

class AdminLoginForm(forms.Form):
  email = forms.EmailField(label="Email")
  password = forms.CharField(label="Password", max_length=254, widget=forms.PasswordInput)