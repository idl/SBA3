# -*- coding: utf-8 -*-
import re
from django import forms
from django.template.defaultfilters import safe
from ..models import School
from ..conditions import if_grad

questions = {
  'q1': 'Do you participate in programs that help students transition from high school to college?',
  'q2': 'Do you have a peer mentor?',
  'q3': 'Do you have a one-on-one faculty mentor?',
  'q4': 'Do you have a one-on-one staff mentor?',
  'q5': 'Do you receive encouraging words from your professors?',
  'q6': 'Do you hear your parents/guardians bragging about you for attending college?',
  'q7': 'Do you parents/guardians give you gifts or money for making good grades?',
  'q8': 'Do your friends encourage you to do well in college?',
  'q9': 'Do you receive encouragement from your church family or community to stay in school?',
  'q10': safe('<span style="font-size:24px;font-weight: 300;">For the next 3 questions, to what extend do you agree with each statement?</span><br><br>My professors expect me to do well in most classes. '),
  'q11': 'My professors make me feel good about my academic work in class.',
  'q12': 'Earning a college degree is the best path to financial security.',
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
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
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
    ('notavailable', 'None were avaliable'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q8': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q9': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q10': (
    ('strongdisagree', 'Strongly Disagree'),
    ('disagree', 'Disagree'),
    ('neutral', 'Neither Agree nor Disagree'),
    ('agree', 'Agree'),
    ('strongagree', 'Strongly Agree'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No comment'),
  ),
  'q11': (
    ('strongdisagree', 'Strongly Disagree'),
    ('disagree', 'Disagree'),
    ('neutral', 'Neither Agree nor Disagree'),
    ('agree', 'Agree'),
    ('strongagree', 'Strongly Agree'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No comment'),
  ),
  'q12': (
    ('strongdisagree', 'Strongly Disagree'),
    ('disagree', 'Disagree'),
    ('neutral', 'Neither Agree nor Disagree'),
    ('agree', 'Agree'),
    ('strongagree', 'Strongly Agree'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No comment'),
  )
}

skips = {
  if_grad: [ 'p6q1', 'p6q2', 'p6q4', 'p6q6', 'p6q7' ]
}

class QuestionsPage6Form(forms.Form):
  q1 = forms.ChoiceField(choices=choices['q1'], label=questions['q1'], widget=forms.RadioSelect)
  q2 = forms.ChoiceField(choices=choices['q2'], label=questions['q2'], widget=forms.RadioSelect)
  q3 = forms.ChoiceField(choices=choices['q3'], label=questions['q3'], widget=forms.RadioSelect)
  q4 = forms.ChoiceField(choices=choices['q4'], label=questions['q4'], widget=forms.RadioSelect)
  q5 = forms.ChoiceField(choices=choices['q5'], label=questions['q5'], widget=forms.RadioSelect)
  q6 = forms.ChoiceField(choices=choices['q6'], label=questions['q6'], widget=forms.RadioSelect)
  q7 = forms.ChoiceField(choices=choices['q7'], label=questions['q7'], widget=forms.RadioSelect)
  q8 = forms.ChoiceField(choices=choices['q8'], label=questions['q8'], widget=forms.RadioSelect)
  q9 = forms.ChoiceField(choices=choices['q9'], label=questions['q9'], widget=forms.RadioSelect)
  q10 = forms.ChoiceField(choices=choices['q10'], label=questions['q10'], widget=forms.RadioSelect)
  q11 = forms.ChoiceField(choices=choices['q11'], label=questions['q11'], widget=forms.RadioSelect)
  q12 = forms.ChoiceField(choices=choices['q12'], label=questions['q12'], widget=forms.RadioSelect)

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