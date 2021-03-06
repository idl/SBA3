# -*- tf-8 -*-
import re
from django import forms
from ..models import School
from ..conditions import if_not_on_campus_class
from questions import questions_4 as questions
from choices import choices_4 as choices


skips = {
  if_not_on_campus_class: [ 'p4q2', 'p4q3', 'p4q4', 'p4q9', 'p4q10', 'p4q11' ]
}

class QuestionsPage4Form(forms.Form):
  q1 = forms.ChoiceField(choices=choices['q1'], label=questions['q1'], widget=forms.RadioSelect(attrs={'data-page-num':'4'}))
  q2 = forms.ChoiceField(choices=choices['q2'], label=questions['q2'], widget=forms.RadioSelect(attrs={'data-page-num':'4'}), required=False)
  q3 = forms.ChoiceField(choices=choices['q3'], label=questions['q3'], widget=forms.RadioSelect(attrs={'data-page-num':'4'}), required=False)
  q4 = forms.ChoiceField(choices=choices['q4'], label=questions['q4'], widget=forms.RadioSelect(attrs={'data-page-num':'4'}), required=False)
  q5 = forms.ChoiceField(choices=choices['q5'], label=questions['q5'], widget=forms.RadioSelect(attrs={'data-page-num':'4'}))
  q6 = forms.ChoiceField(choices=choices['q6'], label=questions['q6'], widget=forms.RadioSelect(attrs={'data-page-num':'4'}))
  q7 = forms.ChoiceField(choices=choices['q7'], label=questions['q7'], widget=forms.RadioSelect(attrs={'data-page-num':'4'}))
  q8 = forms.ChoiceField(choices=choices['q8'], label=questions['q8'], widget=forms.RadioSelect(attrs={'data-page-num':'4'}))
  q9 = forms.ChoiceField(choices=choices['q9'], label=questions['q9'], widget=forms.RadioSelect(attrs={'data-page-num':'4'}), required=False)
  q10 = forms.ChoiceField(choices=choices['q10'], label=questions['q10'], widget=forms.RadioSelect(attrs={'data-page-num':'4'}), required=False)
  q11 = forms.ChoiceField(choices=choices['q11'], label=questions['q11'], widget=forms.RadioSelect(attrs={'data-page-num':'4'}), required=False)

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
        actual_skipped_questions.append('p4'+str(q))
    for q in actual_skipped_questions:
      if q not in skipped_questions_possible:
        is_clean = False
    return is_clean
