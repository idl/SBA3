# -*- coding: utf-8 -*-
import re
from django import forms
from ..models import School
from ..conditions import if_grad, if_not_on_campus_class, if_not_tutoring, if_tutoring
from questions import questions_3 as questions
from choices import choices_3 as choices



skips = {
  if_not_tutoring: [ 'p3q2' ],
  if_tutoring: [ 'p3q3', 'p3q4' ],
  if_grad: [ 'p3q5' ],
  if_not_on_campus_class: [ 'p3q6' ]
}

class QuestionsPage3Form(forms.Form):
  q1 = forms.ChoiceField(choices=choices['q1'], label=questions['q1'], widget=forms.RadioSelect(attrs={'data-page-num':'3'}))
  q2 = forms.IntegerField(label=questions['q2'], min_value=0, max_value=168, required=False, widget=forms.NumberInput(attrs={'data-page-num':'3'}))
  q3 = forms.ChoiceField(choices=choices['q3'], label=questions['q3'], widget=forms.RadioSelect(attrs={'data-page-num':'3'}), required=False)
  q4 = forms.ChoiceField(choices=choices['q4'], label=questions['q4'], widget=forms.RadioSelect(attrs={'data-page-num':'3'}), required=False)
  q5 = forms.ChoiceField(choices=choices['q5'], label=questions['q5'], widget=forms.RadioSelect(attrs={'data-page-num':'3'}), required=False)
  q6 = forms.ChoiceField(choices=choices['q6'], label=questions['q6'], widget=forms.RadioSelect(attrs={'data-page-num':'3'}), required=False)
  q7 = forms.ChoiceField(choices=choices['q7'], label=questions['q7'], widget=forms.RadioSelect(attrs={'data-page-num':'3'}))
  q8 = forms.ChoiceField(choices=choices['q8'], label=questions['q8'], widget=forms.RadioSelect(attrs={'data-page-num':'3'}))
  q9 = forms.ChoiceField(choices=choices['q9'], label=questions['q9'], widget=forms.RadioSelect(attrs={'data-page-num':'3'}))

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
        actual_skipped_questions.append('p3'+str(q))
    for q in actual_skipped_questions:
      if q not in skipped_questions_possible:
        is_clean = False
    return is_clean

