# -*- coding: utf-8 -*-
import re
from django import forms
from django.template.defaultfilters import safe
from ..models import School

questions = {
  'q1': safe('<span style="font-size:24px;font-weight: 300;">For the next three items, please indicate, on average, how much time you spend per day engaged in the following activities:</span><br><br>Social Media (Facebook, Twitter, Instagram…)<br><br>Hours:'),
  'q3': safe('Entertainment (TV, Games, Movies)<br><br>Hours:'),
  'q5': safe('Personal Communication (Phone calls, Text messages, Emails)<br><br>Hours:'),
  'q7': safe('<span style="font-size:24px;font-weight: 300;">In your opinion, what are the top three reasons students struggle in college?</span><br><br>Most Important Reason:'),
  'q8': 'Second Most Important Reason:',
  'q9': 'Third Most Important Reason:',
  'q10': safe('<span style="font-size:24px;font-weight: 300;">In your opinion, what are the top three reasons students succeed in college?</span><br><br>Most Important Reason:'),
  'q11': 'Second Most Important Reason:',
  'q12': 'Third Most Important Reason:',
}

skips = {
}


class QuestionsPage10Form(forms.Form):
  q1 = forms.IntegerField(label=questions['q1'], min_value=-2, max_value=7, widget=forms.NumberInput(attrs={'data-page-num':'10'}))
  q2 = forms.IntegerField(label="Minutes:", min_value=-2, max_value=7, widget=forms.NumberInput(attrs={'data-page-num':'10'}))
  q3 = forms.IntegerField(label=questions['q3'], min_value=-2, max_value=7, widget=forms.NumberInput(attrs={'data-page-num':'10'}))
  q4 = forms.IntegerField(label="Minutes:", min_value=-2, max_value=7, widget=forms.NumberInput(attrs={'data-page-num':'10'}))
  q5 = forms.IntegerField(label=questions['q5'], min_value=-2, max_value=7, widget=forms.NumberInput(attrs={'data-page-num':'10'}))
  q6 = forms.IntegerField(label="Minutes:", min_value=-2, max_value=7, widget=forms.NumberInput(attrs={'data-page-num':'10'}))
  q7 = forms.CharField(label=questions['q7'], widget=forms.TextInput(attrs={'data-page-num':'10'}))
  q8 = forms.CharField(label=questions['q8'], widget=forms.TextInput(attrs={'data-page-num':'10'}))
  q9 = forms.CharField(label=questions['q9'], widget=forms.TextInput(attrs={'data-page-num':'10'}))
  q10 = forms.CharField(label=questions['q10'], widget=forms.TextInput(attrs={'data-page-num':'10'}))
  q11 = forms.CharField(label=questions['q11'], widget=forms.TextInput(attrs={'data-page-num':'10'}))
  q12 = forms.CharField(label=questions['q12'], widget=forms.TextInput(attrs={'data-page-num':'10'}))

  def __init__(self, post_data=None, session=None):
    if post_data:
      super(forms.Form, self).__init__(post_data)
    else:
      super(forms.Form, self).__init__()
    if session:
      for cond in skips.keys():
        for q in skips[cond]:
          q_num = re.compile('^p\d{1,2}(q\d{1,2})$').match(q).group(1)
          print 'for q\'s:\n -', q_num
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
        actual_skipped_questions.append('p10'+str(q))
    for q in actual_skipped_questions:
      if q not in skipped_questions_possible:
        is_clean = False
    return is_clean
