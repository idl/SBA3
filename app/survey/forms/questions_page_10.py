# -*- coding: utf-8 -*-
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


class QuestionsPage10Form(forms.Form):
  q1 = forms.IntegerField(label=questions['q1'], min_value=-2, max_value=7)
  q2 = forms.IntegerField(label="Minutes:", min_value=-2, max_value=7)
  q3 = forms.IntegerField(label=questions['q3'], min_value=-2, max_value=7)
  q4 = forms.IntegerField(label="Minutes:", min_value=-2, max_value=7)
  q5 = forms.IntegerField(label=questions['q5'], min_value=-2, max_value=7)
  q6 = forms.IntegerField(label="Minutes:", min_value=-2, max_value=7)
  q7 = forms.CharField(label=questions['q7'])
  q8 = forms.CharField(label=questions['q8'])
  q9 = forms.CharField(label=questions['q9'])
  q10 = forms.CharField(label=questions['q10'])
  q11 = forms.CharField(label=questions['q11'])
  q12 = forms.CharField(label=questions['q12'])
