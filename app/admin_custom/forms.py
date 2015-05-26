from django import forms
from survey.models import School, Student
from admin_custom.models import User
from django.utils import timezone as tz
from collections import OrderedDict

YEAR_CHOICES = (
  ('2015', '2015'),
  ('2016', '2016'),
  ('2017', '2017'),
  ('2018', '2018'),
  ('2019', '2019'),
  ('2020', '2020'),
  ('2021', '2021'),
  ('2022', '2022'),
  ('2023', '2023'),
  ('2024', '2024'),
  ('2025', '2025'),
  ('2026', '2026'),
  ('2027', '2027'),
  ('2028', '2028'),
  ('2029', '2029'),
  ('2030', '2030'),
)


class AdminLoginForm(forms.Form):
  email = forms.EmailField(label="Email")
  password = forms.CharField(label="Password", max_length=254, widget=forms.PasswordInput)


class SuperadminSelectSchoolForm(forms.Form):
  school = forms.ModelChoiceField(queryset=School.objects.all(), label="")


class SuperadminCreateEditSchoolForm(forms.ModelForm):
  class Meta:
    model = School
    fields = ['name', 'location']


class SuperadminCreateEditAdminForm(forms.ModelForm):
  class Meta:
    model = User
    fields = [ 'email', 'password', 'is_superuser', 'school' ]
    widgets = {
      'email': forms.EmailInput(),
      'password': forms.PasswordInput(),
      'school': forms.Select(attrs=({'id':'id_admin_school'}))
    }
    labels = { 'is_superuser': 'Is Superuser?'}

  def __init__(self, is_modal=False):
    super(forms.ModelForm, self).__init__()
    fields = OrderedDict()
    if is_modal:
      for field in [ 'email', 'change_password', 'password', 'confirm_password', 'is_superuser', 'school' ]:
        if field == 'change_password' or field == 'confirm_password':
          fields[field] = None
        else:
          fields[field] = self.fields[field]
      self.fields = fields
      self.fields['change_password'] = forms.BooleanField(label="Change Password?")
      self.fields['confirm_password'] = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs=({'label': 'Confirm Password'}))
      )
      self.fields['email'].widget.attrs['id'] = 'id_edit_admin_email_modal'
      self.fields['is_superuser'].widget.attrs['id'] = 'id_edit_admin_is_superuser_modal'
      self.fields['school'].widget.attrs['id'] = 'id_edit_admin_school_modal'
      self.fields['password'].widget.attrs['id'] = 'id_edit_admin_password_modal'
      self.fields['password'].widget.attrs['disabled'] = ''
      self.fields['confirm_password'].widget.attrs['id'] = 'id_admin_confirm_password_modal'
      self.fields['confirm_password'].widget.attrs['disabled'] = ''
    else:
      self.fields['email'].widget.attrs['id'] = 'id_create_admin_email'



class SelectSurveyYearForm(forms.Form):
  survey_year = forms.ChoiceField(label="", widget=forms.Select, choices=[])

  def __init__(self, initial_year=None, available_years=None):
    super(forms.Form, self).__init__()
    if initial_year:
      self.fields['survey_year'].initial = initial_year
    if available_years:
      choices = []
      for year in YEAR_CHOICES:
        if int(year[0]) in available_years:
          choices.append((year[0], year[0]))
      self.fields['survey_year'].choices = choices
    else:
      self.fields['survey_year'].choices = YEAR_CHOICES


class AddStudentsBulkForm(forms.Form):
  roster_file = forms.FileField(label="Select Roster File (.csv)")


class AddSingleStudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['uid', 'email']
    labels = { 'uid': 'User Identifier' }