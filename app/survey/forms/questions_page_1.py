# -*- coding: utf-8 -*-
import re
from django import forms
from ..models import School
from ..constants import num_questions_on_page
from ..conditions import if_grad, if_not_distance

questions = {
  'q1': 'What is your class status?',
  'q2': 'What is your major?',
  'q3': 'Did you transfer from a community/junior college?',
  'q4': 'Are you enrolled in a "Distance or Online" degree program at MSU?',
  'q5': 'Have you ever taken a course that meets on campus?',
  'q6': 'Did you attend a pre-kindergarten program?',
  'q7': 'Did you complete any advanced placement courses in high school?',
  'q8': 'Do you consider yourself a first generation college student?',
  'q9': 'Prior to High School, did you personally know anyone who worked in the fields of Science, Technology, Engineering, or Math?',
  'q10': 'Please consider the following statement: Education was encouraged in my family. Would you...',
  'q11': 'In terms of your academic achievement, who contributed to your success the most?',
}

choices = {
  'q1': (
    ('freshman', 'Freshman'),
    ('sophomore', 'Sophomore'),
    ('junior', 'Junior'),
    ('senior', 'Senior'),
    ('master', 'Master'),
    ('doctorate', 'Doctorate'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q2': (
    ('', '--------'),
    ('nocomment', 'No Comment'),
    ('undecided', 'Undecided'),
    ('', '--------'),
    ('accounting', 'Accounting'),
    ('aerospaceengineering', 'Aerospace Engineering'),
    ('agribusiness', 'Agribusiness'),
    ('art', 'Art'),
    ('agriengineering', 'Agricultural Engineering Technology and Business'),
    ('agriinformation', 'Agricultural Information Science'),
    ('agriculture', 'Agricultural Science'),
    ('agronomy', 'Agronomy'),
    ('dairyscience', 'Animal and Dairy Science'),
    ('anthropology', 'Anthropology'),
    ('architecture', 'Architecture'),
    ('art', 'Art'),
    ('biochemistry', 'Biochemistry'),
    ('bioengineering', 'Biological Engineering'),
    ('biology', 'Biological Sciences'),
    ('building', 'Building Construction Science'),
    ('businessadmin', 'Business Administration'),
    ('businessecon', 'Business Economics'),
    ('businessinfo', 'Business Information Systems'),
    ('chemengineering', 'Chemical Engineering'),
    ('chemistry', 'Chemistry'),
    ('civilengineering', 'Civil Engineering'),
    ('communication', 'Communication'),
    ('computerengineering', 'Computer Engineering'),
    ('computerscience', 'Computer Science'),
    ('criminology', 'Criminology'),
    ('culinology', 'Culinology'),
    ('economics', 'Economics Major (Arts and Sciences)'),
    ('educationalpsyc', 'Educational Psychology'),
    ('electricalengineering', 'Electrical Engineering'),
    ('elementaryed', 'Elementary Education'),
    ('english', 'English'),
    ('enviromentalecon', 'Environmental Economics and Management'),
    ('finance', 'Finance'),
    ('foodscience', 'Food Science, Nutrition and Health Promotion'),
    ('foreignlanguage', 'Foreign Language'),
    ('forestry', 'Forestry'),
    ('generallibarts', 'General Liberal Arts'),
    ('generalscience', 'General Science'),
    ('geoscience', 'Geosciences'),
    ('history', 'History'),
    ('horticulture', 'Horticulture'),
    ('humanscience', 'Human Sciences'),
    ('industrialengineering', 'Industrial Engineering'),
    ('industrialtech', 'Industrial Technology'),
    ('informationtech', 'Information Technology Services'),
    ('interdisciplinary', 'Interdisciplinary Studies'),
    ('interiordesign', 'Interior Design'),
    ('kinesiology', 'Kinesiology'),
    ('landscapearchitecture', 'Landscape Architecture'),
    ('landscapecontracting', 'Landscape Contracting'),
    ('management', 'Management'),
    ('marketing', 'Marketing'),
    ('mathematics', 'Mathematics'),
    ('mechanicalengineering', 'Mechanical Engineering'),
    ('medicaltech', 'Medical Technology'),
    ('microbiology', 'Microbiology'),
    ('musiceducation', 'Music Education'),
    ('music', 'Music'),
    ('philosophy', 'Philosophy'),
    ('physics', 'Physics'),
    ('polyscience', 'Political Science'),
    ('pultryscience', 'Poultry Science'),
    ('psychology', 'Psychology'),
    ('secondaryeducation', 'Secondary Education'),
    ('socialwork', 'Social Work'),
    ('sociology', 'Sociology'),
    ('softwareengineering', 'Software Engineering'),
    ('specialeducation', 'Special Education'),
    ('techteachereducation', 'Technology Teacher Education'),
    ('veterinarymedical', 'Veterinary Medical Technology'),
    ('wildlife', 'Wildlife, Fisheries and Aquaculture'),
    ('other', 'Something Else'),
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
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q6': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q7': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notavailable', 'None were avaliable'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q8': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q9': (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment'),
  ),
  'q10': (
    ('strongdisagree', 'Strongly Disagree'),
    ('disagree', 'Disagree'),
    ('neutral', 'Neither Agree nor Disagree'),
    ('agree', 'Agree'),
    ('strongagree', 'Strongly Agree'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No comment'),
  ),
  'q11': (
    ('parent', 'Parent(s)'),
    ('grandparent', 'Grandparents'),
    ('sibling', 'Siblings'),
    ('auntuncle', 'Aunts or Uncles'),
    ('familyfriend', 'Family friends'),
    ('peer', 'Peers'),
    ('teammate', 'Teammates'),
    ('teacher', 'Teacher'),
    ('coach', 'Coach'),
    ('signother', 'Significant Other'),
    ('family', 'Family'),
    ('none', 'None of these'),
    ('notsure', 'Not sure'),
    ('nocomment', 'No comment'),
  )
}

skips = {
  if_grad: [ 'p1q3', 'p1q7' ],
  if_not_distance: [ 'p1q5' ]
}


class QuestionsPage1Form(forms.Form):
  q1 = forms.ChoiceField(choices=choices['q1'], label=questions['q1'], widget=forms.RadioSelect)
  q2 = forms.ChoiceField(choices=choices['q2'], label=questions['q2'])
  q3 = forms.ChoiceField(choices=choices['q3'], label=questions['q3'], widget=forms.RadioSelect)
  q4 = forms.ChoiceField(choices=choices['q4'], label=questions['q4'], widget=forms.RadioSelect)
  q5 = forms.ChoiceField(choices=choices['q5'], label=questions['q5'], widget=forms.RadioSelect)
  q6 = forms.ChoiceField(choices=choices['q6'], label=questions['q6'], widget=forms.RadioSelect)
  q7 = forms.ChoiceField(choices=choices['q7'], label=questions['q7'], widget=forms.RadioSelect)
  q8 = forms.ChoiceField(choices=choices['q8'], label=questions['q8'], widget=forms.RadioSelect)
  q9 = forms.ChoiceField(choices=choices['q9'], label=questions['q9'], widget=forms.RadioSelect)
  q10 = forms.ChoiceField(choices=choices['q10'], label=questions['q10'], widget=forms.RadioSelect)
  q11 = forms.ChoiceField(choices=choices['q11'], label=questions['q11'], widget=forms.RadioSelect)

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

  def clean(self):
    # get all questions that can possibly be skipped for this page
    skipped_questions_possible = []
    actual_skipped_questions = []
    for cond in skips.keys():
      for q in skips[cond]:
        if q not in skipped_questions_possible:
          skipped_questions_possible.append(q)
    print skipped_questions_possible
    for q in self.cleaned_data:
      print q, self.cleaned_data[q]
    # return True

