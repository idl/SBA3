# -*- coding: utf-8 -*-
import re
from django import forms
from ..models import School
from ..conditions import (if_not_organization_member, if_live_on_campus,
                         if_not_on_campus_class,
                         if_not_away_from_home_or_not_live_on_campus,
                         if_not_drink_alcohol, if_not_employed)
from questions import questions_9 as questions
from choices import choices_9 as choices


skips = {
  if_not_organization_member: [ 'p9q2' ],
  if_not_on_campus_class: [ 'p9q3' ],
  if_live_on_campus: [ 'p9q4' ],
  if_not_away_from_home_or_not_live_on_campus: [ 'p9q5' ],
  if_not_drink_alcohol: [ 'p9q8' ]
}

class QuestionsPage9Form(forms.Form):
  q1 = forms.ChoiceField(choices=choices['q1'], label=questions['q1'], widget=forms.RadioSelect(attrs={'data-page-num':'9'}))
  q2 = forms.IntegerField(label=questions['q2'], min_value=-2, max_value=168, required=False, widget=forms.NumberInput(attrs={'data-page-num':'9'}))
  q3 = forms.ChoiceField(choices=choices['q3'], label=questions['q3'], widget=forms.RadioSelect(attrs={'data-page-num':'9'}), required=False)
  q4 = forms.ChoiceField(choices=choices['q4'], label=questions['q4'], widget=forms.RadioSelect(attrs={'data-page-num':'9'}), required=False)
  q5 = forms.IntegerField(label=questions['q5'], min_value=-2, max_value=100, required=False, widget=forms.NumberInput(attrs={'data-page-num':'9'}))
  q6 = forms.IntegerField(label=questions['q6'], min_value=-2, max_value=168, widget=forms.NumberInput(attrs={'data-page-num':'9'}))
  q7 = forms.ChoiceField(choices=choices['q7'], label=questions['q7'], widget=forms.RadioSelect(attrs={'data-page-num':'9'}))
  q8 = forms.IntegerField(label=questions['q8'], min_value=-2, max_value=40, required=False, widget=forms.NumberInput(attrs={'data-page-num':'9'}))
  q9 = forms.IntegerField(label=questions['q9'], min_value=-2, max_value=24, widget=forms.NumberInput(attrs={'data-page-num':'9'}))
  q10 = forms.IntegerField(label=questions['q10'], min_value=-2, max_value=7, widget=forms.NumberInput(attrs={'data-page-num':'9'}))
  q11 = forms.IntegerField(label=questions['q11'], min_value=-2, max_value=7, widget=forms.NumberInput(attrs={'data-page-num':'9'}))

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
        actual_skipped_questions.append('p9'+str(q))
    for q in actual_skipped_questions:
      if q not in skipped_questions_possible:
        is_clean = False
    return is_clean
