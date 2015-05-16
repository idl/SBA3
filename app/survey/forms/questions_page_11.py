# -*- coding: utf-8 -*-
import re
from django import forms
from django.template.defaultfilters import safe
from ..models import School
from ..conditions import if_grad, if_not_employed

questions = {
  'q1': safe('What is your age?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q2': 'What is your gender?',
  'q3': 'Are you currently employed?',
  'q4': 'Do you work on or off campus?',
  'q5': safe('On average, how many hours per week do you work?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q6': 'Do you work anytime between the hours of 5pm - 12am?',
  'q7': 'What is the highest level of education completed by your mother?',
  'q8': 'What is the highest level of education completed by your father?',
  'q9': 'In general, how would you describe the racial mix of your high school?',
  'q10': 'Which category best describes your race?',
  'q11': 'Do you have friends of other ethnic groups?',
  'q12': 'Do you receive the Pell grant?',
  'q13': 'While in high school, did you qualify for or receive free or reduced priced lunch?',
  'q14': 'In your opinion, did the majority of students in your high school receive free or reduced priced lunch?',
}

choices = {
  'q2': (
    ('female', 'Female'),
    ('male', 'Male'),
    ('nocomment', 'No Comment'),
  ),
  'q3': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q4': (
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
    ('none','No formal education'),
    ('somehighschool','Some High School or less'),
    ('highschool','High School Diploma or GED'),
    ('somecollege','Some college, did not complete degree'),
    ('associate','Associate Degree'),
    ('bachelor','Bachelor\'s Degree (B.S., B.A.)'),
    ('master','Master\'s Degree (M.S., M.A)'),
    ('professional','Professional Degree (MD, JD, EdD, PsyD, ect.)'),
    ('doctorate','Doctorate Degree (Ph.D.)'),
    ('notsure','Not Sure'),
    ('nodcomment','No comment'),
  ),
  'q8': (
    ('none','No formal education'),
    ('somehighschool','Some High School or less'),
    ('highschool','High School Diploma or GED'),
    ('somecollege','Some college, did not complete degree'),
    ('associate','Associate Degree'),
    ('bachelor','Bachelor\'s Degree (B.S., B.A.)'),
    ('master','Master\'s Degree (M.S., M.A)'),
    ('professional','Professional Degree (MD, JD, EdD, PsyD, ect.)'),
    ('doctorate','Doctorate Degree (Ph.D.)'),
    ('notsure','Not Sure'),
    ('nodcomment','No comment'),
  ),
  'q9': (
    ('black', 'Majority Black'),
    ('white', 'Majority White'),
    ('neutral', 'About Equal'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No comment'),
  ),
  'q10': (
    ('black', 'African American'),
    ('white', 'White/ Caucasian'),
    ('asian', 'Asian American'),
    ('hispanic', 'Hispanic/Latino'),
    ('native', 'Native American'),
    ('pasific', 'Pacific Islander'),
    ('multi', 'Multi-racial'),
    ('nocomment', 'No comment'),
  ),
  'q11': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q12': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q13': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q14': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
}

skips = {
  if_grad: [ 'p11q12' ],
  if_not_employed: [ 'p11q4', 'p11q5', 'p11q6' ]
}

class QuestionsPage11Form(forms.Form):
  q1 = forms.IntegerField(label=questions['q1'], min_value=-2, max_value=100)
  q2 = forms.ChoiceField(choices=choices['q2'], label=questions['q2'], widget=forms.RadioSelect)
  q3 = forms.ChoiceField(choices=choices['q3'], label=questions['q3'], widget=forms.RadioSelect)
  q4 = forms.ChoiceField(choices=choices['q4'], label=questions['q4'], widget=forms.RadioSelect, required=False)
  q5 = forms.IntegerField(label=questions['q5'], min_value=-2, max_value=80, required=False)
  q6 = forms.ChoiceField(choices=choices['q6'], label=questions['q6'], widget=forms.RadioSelect, required=False)
  q7 = forms.ChoiceField(choices=choices['q7'], label=questions['q7'], widget=forms.RadioSelect)
  q8 = forms.ChoiceField(choices=choices['q8'], label=questions['q8'], widget=forms.RadioSelect)
  q9 = forms.ChoiceField(choices=choices['q9'], label=questions['q9'], widget=forms.RadioSelect)
  q10 = forms.ChoiceField(choices=choices['q10'], label=questions['q10'], widget=forms.RadioSelect)
  q11 = forms.ChoiceField(choices=choices['q11'], label=questions['q11'], widget=forms.RadioSelect)
  q12 = forms.ChoiceField(choices=choices['q12'], label=questions['q12'], widget=forms.RadioSelect, required=False)
  q13 = forms.ChoiceField(choices=choices['q13'], label=questions['q13'], widget=forms.RadioSelect)
  q14 = forms.ChoiceField(choices=choices['q14'], label=questions['q14'], widget=forms.RadioSelect)

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
        actual_skipped_questions.append('p11'+str(q))
    for q in actual_skipped_questions:
      if q not in skipped_questions_possible:
        is_clean = False
    return is_clean
