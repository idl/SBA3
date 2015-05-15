# -*- coding: utf-8 -*-
import re
from django import forms
from django.template.defaultfilters import safe # http://stackoverflow.com/questions/16782116/django-form-field-label-as-html
from ..models import School
from ..conditions import if_on_campus_class

questions = {
  'q1': 'While growing up, did you have a mentor?',
  'q2': 'Do you have a mentor now?',
  'q3': 'Do you see role models on campus?',
  'q4': 'How would you rate your time management skills?',
  'q5': 'Do you routinely use a calendar or daily planner (paper or digital)?',
  'q6': 'Do you review your class notes after class?',
  'q7': 'In general, do you study for tests by yourself?',
  'q8': 'Select the type of learning style that describes you best:',
  'q9': safe('On average, how many hours per DAY do you spend studying?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q10': safe('On average how many days in advance do you begin studying for upcoming exams?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q11': safe('In general, how many class sessions do you miss over the course of a semester?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
}

choices = {
  'q1': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q2': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q3': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q4': (
    ('poor', 'Poor'),
    ('belowaverage', 'Below Average'),
    ('average', 'Average'),
    ('aboveaverage', 'Above Average'),
    ('excellent', 'Excellent'),
  ),
  'q5': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q6': (
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
  'q8': (
    ('visual', 'Visual (Seeing)'),
    ('auditory', 'Auditory (Hearing)'),
    ('kinsethetics', 'Kinesthetics (Hands-on)'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  )
}

skips = {
  if_on_campus_class: [ 'p2q3', 'p2q6', 'p2q11' ]
}

class QuestionsPage2Form(forms.Form):
  q1 = forms.ChoiceField(choices=choices['q1'], label=questions['q1'], widget=forms.RadioSelect)
  q2 = forms.ChoiceField(choices=choices['q2'], label=questions['q2'], widget=forms.RadioSelect)
  q3 = forms.ChoiceField(choices=choices['q3'], label=questions['q3'], widget=forms.RadioSelect)
  q4 = forms.ChoiceField(choices=choices['q4'], label=questions['q4'], widget=forms.RadioSelect)
  q5 = forms.ChoiceField(choices=choices['q5'], label=questions['q5'], widget=forms.RadioSelect)
  q6 = forms.ChoiceField(choices=choices['q6'], label=questions['q6'], widget=forms.RadioSelect)
  q7 = forms.ChoiceField(choices=choices['q7'], label=questions['q7'], widget=forms.RadioSelect)
  q8 = forms.ChoiceField(choices=choices['q8'], label=questions['q8'], widget=forms.RadioSelect)
  q9 = forms.IntegerField(label=questions['q9'], min_value=-2, max_value=24)
  q10 = forms.IntegerField(label=questions['q10'], min_value=-2, max_value=24)
  q11 = forms.IntegerField(label=questions['q11'], min_value=-2, max_value=24)

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

  def clean(self):
    # get all questions that can possibly be skipped for this page
    skipped_questions_possible = []
    actual_skipped_questions = []
    for cond in skips.keys():
      for q in skips[cond]:
        if q not in skipped_questions_possible:
          skipped_questions_possible.append(q)
    print skipped_questions_possible
    for q in self.cleaned_data:
      print q, self.cleaned_data[q]
    # return True