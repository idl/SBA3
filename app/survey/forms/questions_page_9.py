# -*- coding: utf-8 -*-
import re
from django import forms
from django.template.defaultfilters import safe
from ..models import School
from ..conditions import if_grad

questions = {
  'q1': 'Do you belong to any student organizations?',
  'q2': safe('How many hours per week do you spend doing student organization related services or activities?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q3': 'Do you live on or off campus?',
  'q4': 'While attending college, do you live away from home?',
  'q5': safe('How many times per semester do you go home?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q6': safe('On average, how many hours per week do you spend partying?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q7': 'Do you drink alcoholic beverages?',
  'q8': safe('On days that you drink, about how many drinks do you consume?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q9': safe('On average, how many hours of sleep do you get on a weeknight?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q10': safe('How many days per week do you exercise for at least 15 minutes?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q11': safe('How many days during the week do you eat a nutritious (e.g., fruits, vegetable, nuts, lean meats etc) meal for breakfast?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q12': safe('How many days during the week do you eat a nutritious (e.g., fruits, vegetable, nuts, lean meats etc) meal for lunch?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q13': safe('How many days during the week do you eat a nutritious (e.g., fruits, vegetable, nuts, lean meats etc) meal for dinner?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
}

choices = {
  'q1': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q3': (
    ('on', 'On Campus'),
    ('off', 'Off Campus'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q4': (
    ('on', 'On Campus'),
    ('off', 'Off Campus'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q7': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notavailable', 'None were avaliable'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
}

skips = {
}

class QuestionsPage9Form(forms.Form):
  q1 = forms.ChoiceField(choices=choices['q1'], label=questions['q1'], widget=forms.RadioSelect)
  q2 = forms.IntegerField(label=questions['q2'], min_value=-2, max_value=168)
  q3 = forms.ChoiceField(choices=choices['q3'], label=questions['q3'], widget=forms.RadioSelect)
  q4 = forms.ChoiceField(choices=choices['q4'], label=questions['q4'], widget=forms.RadioSelect)
  q5 = forms.IntegerField(label=questions['q5'], min_value=-2, max_value=100)
  q6 = forms.IntegerField(label=questions['q6'], min_value=-2, max_value=168)
  q7 = forms.ChoiceField(choices=choices['q7'], label=questions['q7'], widget=forms.RadioSelect)
  q8 = forms.IntegerField(label=questions['q8'], min_value=-2, max_value=40)
  q9 = forms.IntegerField(label=questions['q9'], min_value=-2, max_value=24)
  q10 = forms.IntegerField(label=questions['q10'], min_value=-2, max_value=7)
  q11 = forms.IntegerField(label=questions['q11'], min_value=-2, max_value=7)

  def __init__(self, post_data=None, session=None):
    super(forms.Form, self).__init__(post_data)
    if post_data and session:
      result_set = {}
      for cond in skips.keys():
        if cond(session):
          for q in skips[cond]:
            print "cond true:", cond, "      hiding", q
            q_num = re.compile('^p\d{1,2}(q\d{1,2})$').match(q).group(1)
            self.fields[q_num].widget.attrs['class'] = 'q_debug'