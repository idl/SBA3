# -*- coding: utf-8 -*-
from django import forms
from django.template.defaultfilters import safe
from ..models import School

questions = {
  'q1': 'Are you currently attending tutoring sessions?',
  'q2': 'On average, how many hours do you spend in tutoring sessions per week?',
  'q3': 'Would you attend tutoring sessions if they were freely available?',
  'q4': 'Have you looked for tutoring help?',
  'q5': 'Compared to high school, has the time you spend studying for classes...',
  'q6': '<span style="font-size:24px;font-weight: 300;">How often do you do the following?</span><br><br>(1) Show up late for class',
  'q7': '(2) Turn assignments in late or incomplete',
  'q8': '(3) Miss an exam or quiz',
  'q9': '(4) Seek extra credit to improve a grade',
}

choices = {
  'q1': (
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
    ('decressed', 'Decreased '),
    ('increased', 'Increased'),
    ('same', 'Stayed the same'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q6': (
    ('never', 'Never'),
    ('rarely', 'Rarely'),
    ('some', 'Some'),
    ('often', 'Often'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q7': (
    ('never', 'Never'),
    ('rarely', 'Rarely'),
    ('some', 'Some'),
    ('often', 'Often'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q8': (
    ('never', 'Never'),
    ('rarely', 'Rarely'),
    ('some', 'Some'),
    ('often', 'Often'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q9': (
    ('never', 'Never'),
    ('rarely', 'Rarely'),
    ('some', 'Some'),
    ('often', 'Often'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
}

class QuestionsPage3Form(forms.Form):
  q1 = forms.ChoiceField(choices=choices['q1'], label=questions['q1'], widget=forms.RadioSelect)
  q2 = forms.IntegerField(label=questions['q2'], min_value=0, max_value=168)
  q3 = forms.ChoiceField(choices=choices['q3'], label=questions['q3'], widget=forms.RadioSelect)
  q4 = forms.ChoiceField(choices=choices['q4'], label=questions['q4'], widget=forms.RadioSelect)
  q5 = forms.ChoiceField(choices=choices['q5'], label=questions['q5'], widget=forms.RadioSelect)
  q6 = forms.ChoiceField(choices=choices['q6'], label=safe(questions['q6']), widget=forms.RadioSelect)
  q7 = forms.ChoiceField(choices=choices['q7'], label=questions['q7'], widget=forms.RadioSelect)
  q8 = forms.ChoiceField(choices=choices['q8'], label=questions['q8'], widget=forms.RadioSelect)
  q9 = forms.ChoiceField(choices=choices['q9'], label=questions['q9'], widget=forms.RadioSelect)
