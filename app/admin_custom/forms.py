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
)


class AdminLoginForm(forms.Form):
  email = forms.EmailField(label="Email")
  password = forms.CharField(label="Password", max_length=254, widget=forms.PasswordInput)


class SelectSurveyYearForm(forms.Form):
  survey_year = forms.ChoiceField(label="", widget=forms.Select, choices=YEAR_CHOICES)

  def __init__(self, initial_year=None):
    super(forms.Form, self).__init__()
    if initial_year:
      self.fields['survey_year'].initial = initial_year
