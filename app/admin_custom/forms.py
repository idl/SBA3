from django import forms
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


class SelectSurveyYearForm(forms.Form):
  survey_year = forms.ChoiceField(label="", widget=forms.Select, choices=[])

  def __init__(self, initial_year=None, available_years=None):
    super(forms.Form, self).__init__()
    if initial_year:
      self.fields['survey_year'].initial = initial_year
    if available_years:
      choices = []
      for year in YEAR_CHOICES:
        choices.append((year, year))
      print choices
      # self.fields['survey_year'].choices
    else:
      self.fields['survey_year'].choices = YEAR_CHOICES

