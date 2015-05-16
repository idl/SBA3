# -*- coding: utf-8 -*-
import re
from django import forms
from django.template.defaultfilters import safe
from ..models import School
from ..conditions import if_grad, if_not_on_campus_class, if_not_tutoring, if_tutoring

questions = {
  'q1': 'Are you currently attending tutoring sessions?',
  'q2': 'On average, how many hours do you spend in tutoring sessions per week?',
  'q3': 'Would you attend tutoring sessions if they were freely available?',
  'q4': 'Have you looked for tutoring help?',
  'q5': 'Compared to high school, has the time you spend studying for classes...',
  'q6': safe('<span style="font-size:24px;font-weight: 300;">How often do you do the following?</span><br><br>(1) Show up late for class'),
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

skips = {
  if_not_tutoring: [ 'p3q2' ],
  if_tutoring: [ 'p3q3', 'p3q4' ],
  if_grad: [ 'p3q5' ],
  if_not_on_campus_class: [ 'p3q6' ]
}

class QuestionsPage3Form(forms.Form):
  q1 = forms.ChoiceField(choices=choices['q1'], label=questions['q1'], widget=forms.RadioSelect)
  q2 = forms.IntegerField(label=questions['q2'], min_value=0, max_value=168, required=False)
  q3 = forms.ChoiceField(choices=choices['q3'], label=questions['q3'], widget=forms.RadioSelect, required=False)
  q4 = forms.ChoiceField(choices=choices['q4'], label=questions['q4'], widget=forms.RadioSelect, required=False)
  q5 = forms.ChoiceField(choices=choices['q5'], label=questions['q5'], widget=forms.RadioSelect, required=False)
  q6 = forms.ChoiceField(choices=choices['q6'], label=questions['q6'], widget=forms.RadioSelect, required=False)
  q7 = forms.ChoiceField(choices=choices['q7'], label=questions['q7'], widget=forms.RadioSelect)
  q8 = forms.ChoiceField(choices=choices['q8'], label=questions['q8'], widget=forms.RadioSelect)
  q9 = forms.ChoiceField(choices=choices['q9'], label=questions['q9'], widget=forms.RadioSelect)

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
        actual_skipped_questions.append('p3'+str(q))
    for q in actual_skipped_questions:
      if q not in skipped_questions_possible:
        is_clean = False
    return is_clean

