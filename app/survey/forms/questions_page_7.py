# -*- coding: utf-8 -*-
import re
from django import forms
from ..models import School
from ..conditions import if_grad
from questions import questions_7 as questions
from choices import choices_7 as choices

skips = {
  if_grad: [ 'p7q2', 'p7q9' ]
}

class QuestionsPage7Form(forms.Form):
  q1 = forms.ChoiceField(choices=choices['q1'], label=questions['q1'], widget=forms.RadioSelect(attrs={'data-page-num':'7'}))
  q2 = forms.ChoiceField(choices=choices['q2'], label=questions['q2'], widget=forms.RadioSelect(attrs={'data-page-num':'7'}), required=False)
  q3 = forms.ChoiceField(choices=choices['q3'], label=questions['q3'], widget=forms.RadioSelect(attrs={'data-page-num':'7'}))
  q4 = forms.ChoiceField(choices=choices['q4'], label=questions['q4'], widget=forms.RadioSelect(attrs={'data-page-num':'7'}))
  q5 = forms.ChoiceField(choices=choices['q5'], label=questions['q5'], widget=forms.RadioSelect(attrs={'data-page-num':'7'}))
  q6 = forms.IntegerField(label=questions['q6'], min_value=-2, max_value=36, widget=forms.NumberInput(attrs={'data-page-num':'7'}))
  q7 = forms.FloatField(label=questions['q7'], min_value=-2, max_value=5, widget=forms.NumberInput(attrs={'step':'0.1', 'data-page-num':'7'}))
  q8 = forms.FloatField(label=questions['q8'], min_value=-2, max_value=5, widget=forms.NumberInput(attrs={'step':'0.1', 'data-page-num':'7'}))
  q9 = forms.IntegerField(label=questions['q9'], min_value=-2, max_value=50, widget=forms.NumberInput(attrs={'data-page-num':'7'}), required=False)

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
        actual_skipped_questions.append('p7'+str(q))
    for q in actual_skipped_questions:
      if q not in skipped_questions_possible:
        is_clean = False
    return is_clean
