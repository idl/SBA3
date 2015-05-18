from django import forms
from ..models import School

class SurveyContinueForm(forms.Form):
  school = forms.ModelChoiceField(queryset=School.objects.all())
  student_uid = forms.CharField(label="Student Identifier", max_length=24, widget=forms.TextInput(attrs={'placeholder':''}))
  continue_pass = forms.CharField(label="Continuation Passkey", max_length=24, widget=forms.TextInput(attrs={'placeholder':''}))


