# -*- coding: utf-8 -*-
import re
from django import forms
from django.template.defaultfilters import safe
from ..models import School
from ..conditions import (if_not_organization_member, if_live_on_campus,
                         if_not_on_campus_class,
                         if_not_away_from_home_or_not_live_on_campus,
                         if_not_drink_alcohol, if_not_employed)

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
    ('oncampus', 'On Campus'),
    ('offcampus', 'Off Campus'),
    ('nocomment', 'No Comment'),
  ),
  'q4': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q7': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
}

skips = {
  if_not_organization_member: [ 'p9q2' ],
  if_not_on_campus_class: [ 'p9q3' ],
  if_live_on_campus: [ 'p9q4' ],
  if_not_away_from_home_or_not_live_on_campus: [ 'p9q5' ],
  if_not_drink_alcohol: [ 'p9q8' ]
}

class QuestionsPage9Form(forms.Form):
  q1 = forms.ChoiceField(choices=choices['q1'], label=questions['q1'], widget=forms.RadioSelect)
  q2 = forms.IntegerField(label=questions['q2'], min_value=-2, max_value=168, required=False)
  q3 = forms.ChoiceField(choices=choices['q3'], label=questions['q3'], widget=forms.RadioSelect, required=False)
  q4 = forms.ChoiceField(choices=choices['q4'], label=questions['q4'], widget=forms.RadioSelect, required=False)
  q5 = forms.IntegerField(label=questions['q5'], min_value=-2, max_value=100, required=False)
  q6 = forms.IntegerField(label=questions['q6'], min_value=-2, max_value=168)
  q7 = forms.ChoiceField(choices=choices['q7'], label=questions['q7'], widget=forms.RadioSelect)
  q8 = forms.IntegerField(label=questions['q8'], min_value=-2, max_value=40, required=False)
  q9 = forms.IntegerField(label=questions['q9'], min_value=-2, max_value=24)
  q10 = forms.IntegerField(label=questions['q10'], min_value=-2, max_value=7)
  q11 = forms.IntegerField(label=questions['q11'], min_value=-2, max_value=7)

  def __init__(self, post_data=None, session=None):
    if post_data:
      super(forms.Form, self).__init__(post_data)
    else:
      super(forms.Form, self).__init__()
    if session:
      for cond in skips.keys():
        if cond(session):
          print 'cond true: ', cond
          for q in skips[cond]:
            q_num = re.compile('^p\d{1,2}(q\d{1,2})$').match(q).group(1)
            print 'for q\'s:\n -', q_num
            self.fields[q_num].widget.attrs['class'] = 'q_hidden'
            self.fields[q_num].widget.attrs['data-condition-class'] = cond.__name__

  def clean(self):
    # get all questions that can possibly be skipped for this page
    skipped_questions_possible = []
    actual_skipped_questions = []
    is_clean = True
    for cond in skips.keys():
      for q in skips[cond]:
        if q not in skipped_questions_possible:
          skipped_questions_possible.append(q)
    for q in self.cleaned_data:
      if q not in skipped_questions_possible:
        actual_skipped_questions.append('p9'+str(q))
    for q in actual_skipped_questions:
      if q not in skipped_questions_possible:
        is_clean = False
    return is_clean
