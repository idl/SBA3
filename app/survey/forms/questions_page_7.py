# -*- coding: utf-8 -*-
from django import forms
from django.template.defaultfilters import safe
from ..models import School

questions = {
  'q1': 'What Letter Grade do YOU expect to make at MSU?',
  'q2': 'What Letter Grade do your PARENT(S)/ GUARDIAN(S) expect you to make at MSU?',
  'q3': 'What Letter Grade do your TEACHERS/ PROFESSORS expect you to make at MSU?',
  'q4': 'What Letter Grade do your CLOSE FRIENDS expect you to make at MSU?',
  'q5': 'What Letter Grade do your BROTHER(S)/ SISTER(S) expect you to make at MSU?',
  'q6': safe('What was your highest ACT Score?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q7': safe('What was your overall grade point average (GPA) in High School?<br>(<code>-1.0</code> for Not Sure, <code>-2.0</code> for No Comment)'),
  'q8': safe('What was your overall grade point average (GPA) in College?<br>(<code>-1.0</code> for Not Sure, <code>-2.0</code> for No Comment)'),
  'q9': safe('How many on-line classes have you completed with a grade of less than "C" at MSU?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
}


choices = {
  'q1': (
    ('a','A'),
    ('b','B'),
    ('c','C'),
    ('d','D'),
    ('f','F'),
    ('notsure','Not Sure'),
    ('nocomment','No Comment'),
  ),
  'q2': (
    ('a','A'),
    ('b','B'),
    ('c','C'),
    ('d','D'),
    ('f','F'),
    ('notsure','Not Sure'),
    ('nocomment','No Comment'),
  ),
  'q3': (
    ('a','A'),
    ('b','B'),
    ('c','C'),
    ('d','D'),
    ('f','F'),
    ('notsure','Not Sure'),
    ('nocomment','No Comment'),
  ),
  'q4': (
    ('a','A'),
    ('b','B'),
    ('c','C'),
    ('d','D'),
    ('f','F'),
    ('notsure','Not Sure'),
    ('nocomment','No Comment'),
  ),
  'q5': (
    ('a','A'),
    ('b','B'),
    ('c','C'),
    ('d','D'),
    ('f','F'),
    ('notsure','Not Sure'),
    ('nocomment','No Comment'),
  ),
}

class QuestionsPage7Form(forms.Form):
  q1 = forms.ChoiceField(choices=choices['q1'], label=questions['q1'], widget=forms.RadioSelect)
  q2 = forms.ChoiceField(choices=choices['q2'], label=questions['q2'], widget=forms.RadioSelect)
  q3 = forms.ChoiceField(choices=choices['q3'], label=questions['q3'], widget=forms.RadioSelect)
  q4 = forms.ChoiceField(choices=choices['q4'], label=questions['q4'], widget=forms.RadioSelect)
  q5 = forms.ChoiceField(choices=choices['q5'], label=questions['q5'], widget=forms.RadioSelect)
  q6 = forms.IntegerField(label=questions['q6'], min_value=-2, max_value=36)
  q7 = forms.FloatField(label=questions['q7'], min_value=-2, max_value=5, widget=forms.NumberInput(attrs={'step':'0.1'}))
  q8 = forms.FloatField(label=questions['q8'], min_value=-2, max_value=5, widget=forms.NumberInput(attrs={'step':'0.1'}))
  q9 = forms.IntegerField(label=questions['q9'], min_value=-2, max_value=50)
