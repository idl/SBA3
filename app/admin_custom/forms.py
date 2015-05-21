from django import forms
from survey.models import School
from django.utils import timezone as tz

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

class SuperadminCreateSchoolForm(forms.ModelForm):
  class Meta:
    model = School
    fields = ['name', 'location', 'survey_title']

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

