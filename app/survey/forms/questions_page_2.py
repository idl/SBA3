# -*- coding: utf-8 -*-
import re
from django import forms # http://stackoverflow.com/questions/16782116/django-form-field-label-as-html
from ..models import School
from ..conditions import if_not_on_campus_class
from questions import questions_2 as questions
from choices import choices_2 as choices


skips = {
  if_not_on_campus_class: [ 'p2q3', 'p2q6', 'p2q11' ]
}

class QuestionsPage2Form(forms.Form):
  q1 = forms.ChoiceField(choices=choices['q1'], label=questions['q1'], widget=forms.RadioSelect(attrs={'data-page-num':'2'}))
  q2 = forms.ChoiceField(choices=choices['q2'], label=questions['q2'], widget=forms.RadioSelect(attrs={'data-page-num':'2'}))
  q3 = forms.ChoiceField(choices=choices['q3'], label=questions['q3'], widget=forms.RadioSelect(attrs={'data-page-num':'2'}), required=False)
  q4 = forms.ChoiceField(choices=choices['q4'], label=questions['q4'], widget=forms.RadioSelect(attrs={'data-page-num':'2'}))
  q5 = forms.ChoiceField(choices=choices['q5'], label=questions['q5'], widget=forms.RadioSelect(attrs={'data-page-num':'2'}))
  q6 = forms.ChoiceField(choices=choices['q6'], label=questions['q6'], widget=forms.RadioSelect(attrs={'data-page-num':'2'}), required=False)
  q7 = forms.ChoiceField(choices=choices['q7'], label=questions['q7'], widget=forms.RadioSelect(attrs={'data-page-num':'2'}))
  q8 = forms.ChoiceField(choices=choices['q8'], label=questions['q8'], widget=forms.RadioSelect(attrs={'data-page-num':'2'}))
  q9 = forms.IntegerField(label=questions['q9'], min_value=-2, max_value=24, widget=forms.NumberInput(attrs={'data-page-num':'2'}))
  q10 = forms.IntegerField(label=questions['q10'], min_value=-2, max_value=24, widget=forms.NumberInput(attrs={'data-page-num':'2'}))
  q11 = forms.IntegerField(label=questions['q11'], min_value=-2, max_value=24, required=False, widget=forms.NumberInput(attrs={'data-page-num':'2'}))

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
        actual_skipped_questions.append('p2'+str(q))
    for q in actual_skipped_questions:
      if q not in skipped_questions_possible:
        is_clean = False
    return is_clean
