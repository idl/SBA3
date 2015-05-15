# -*- coding: utf-8 -*-
import re
from django import forms
from django.template.defaultfilters import safe
from ..models import School
from ..conditions import if_grad

questions = {
  'q1': 'Did you attend a Student Orientation session before starting college?',
  'q2': 'Did your parents (or guardians) attend an orientation session with you?',
  'q3': 'Do you share your grades with your parent(s) or legal guardian(s)?',
  'q4': 'Do your parents (or guardians) require you to maintain a certain GPA in college?',
  'q5': 'Do you believe you were academically prepared for college?',
  'q6': '<span style="font-size:24px;font-weight: 300;">Given your academic performance in college, to what extend do you agree with the following statements?</span><br><br>I should have read more books before college.',
  'q7': 'I should have taken more math courses in high school.',
  'q8': 'I should have taken more science courses in high school.',
  'q9': 'I should have paid more attention in classes.',
  'q10': 'I should have worked harder on written assignments.',
  'q11': 'I should have worked with a tutor.',
  'q12': 'I should have enrolled in a program to improve studying skills.',
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
    ('strongdisagree', 'Strongly Disagree'),
    ('disagree', 'Disagree'),
    ('neutral', 'Neither Agree nor Disagree'),
    ('agree', 'Agree'),
    ('strongagree', 'Strongly Agree'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No comment'),
  ),
  'q7': (
    ('strongdisagree', 'Strongly Disagree'),
    ('disagree', 'Disagree'),
    ('neutral', 'Neither Agree nor Disagree'),
    ('agree', 'Agree'),
    ('strongagree', 'Strongly Agree'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No comment'),
  ),
  'q8': (
    ('strongdisagree', 'Strongly Disagree'),
    ('disagree', 'Disagree'),
    ('neutral', 'Neither Agree nor Disagree'),
    ('agree', 'Agree'),
    ('strongagree', 'Strongly Agree'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No comment'),
  ),
  'q9': (
    ('strongdisagree', 'Strongly Disagree'),
    ('disagree', 'Disagree'),
    ('neutral', 'Neither Agree nor Disagree'),
    ('agree', 'Agree'),
    ('strongagree', 'Strongly Agree'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No comment'),
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
  ),
}

skips = {
  if_grad: [ 'p8q2', 'p8q3', 'p8q4' ]
}

class QuestionsPage8Form(forms.Form):
  q1 = forms.ChoiceField(choices=choices['q1'], label=questions['q1'], widget=forms.RadioSelect)
  q2 = forms.ChoiceField(choices=choices['q2'], label=questions['q2'], widget=forms.RadioSelect)
  q3 = forms.ChoiceField(choices=choices['q3'], label=questions['q3'], widget=forms.RadioSelect)
  q4 = forms.ChoiceField(choices=choices['q4'], label=questions['q4'], widget=forms.RadioSelect)
  q5 = forms.ChoiceField(choices=choices['q5'], label=questions['q5'], widget=forms.RadioSelect)
  q6 = forms.ChoiceField(choices=choices['q6'], label=safe(questions['q6']), widget=forms.RadioSelect)
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