import hashlib
import collections
import json
from django.db import models
from django.utils import timezone as tz
from jsonfield import JSONField
from survey.forms.choices import choices_1
from survey.forms.choices import choices_2
from survey.forms.choices import choices_3
from survey.forms.choices import choices_4
from survey.forms.choices import choices_5
from survey.forms.choices import choices_6
from survey.forms.choices import choices_7
from survey.forms.choices import choices_8
from survey.forms.choices import choices_9
from survey.forms.choices import choices_10
from survey.forms.choices import choices_11
from .constants import num_questions_on_page, num_questions_so_far

questions_page_choices = {
  '1': choices_1,
  '2': choices_2,
  '3': choices_3,
  '4': choices_4,
  '5': choices_5,
  '6': choices_6,
  '7': choices_7,
  '8': choices_8,
  '9': choices_9,
  '10': choices_10,
  '11': choices_11
}


class SchoolManager(models.Manager):
  def has_uid(self, uid):
    students = Student.objects.filter(school=self.model)
    print students

class School(models.Model):
  name = models.CharField(max_length=75, blank=False)
  location = models.CharField(max_length=125,
    help_text='Please enter the city and state of the school.')
  survey_title = models.CharField(max_length=50, blank=True, default="")
  date_created = models.DateField(default=tz.now().today())

  objects = SchoolManager()

  def get_survey_years(self):
    years = []
    for student in self.student_set.all():
      for rs in student.resultset_set.all():
        if rs.year not in years:
          years.append(rs.year)
    return years

  def has_surveys(self):
    return len(self.get_survey_years()) > 0

  def __unicode__(self):
    return self.name

  class Meta:
    db_table = u'School'














class StudentManager(models.Manager):
  def create_student(self, uid, email, school):
    print school.student_set
    continue_hash = hashlib.sha256(uid + school.name + email).hexdigest()
    continue_pass = continue_hash[:10]

    student = self.model(
      uid=uid,
      school=school,
      email=email,
      continue_pass=continue_pass
    ).save()

    return student


class Student(models.Model):
  school = models.ForeignKey(School)
  email = models.EmailField(default="", blank=False)
  continue_pass = models.CharField(max_length=10, blank=False)
  uid = models.CharField(max_length=25, blank=False)

  objects = StudentManager()

  def has_started_survey_for_year(self, year):
    if self.get_result_set_for_year(year) == None:
      return False
    return True

  def has_started_survey_for_current_year(self):
    if self.get_result_set_for_year(tz.now().year) == None:
      return False
    return True

  def has_completed_survey_for_current_year(self):
    if self.get_result_set_for_current_year() == None:
      return False
    else:
      if self.get_result_set_for_current_year().completed:
        return True
    return False

  def has_completed_survey_for_year(self, year):
    if self.get_result_set_for_year(year) == None:
      return False
    else:
      if self.get_result_set_for_year(year).completed:
        return True
    return False

  def get_result_set_for_year(self, year):
    try:
      return self.resultset_set.get(year=year)
    except:
      return None
    return None

  def get_result_set_for_current_year(self):
    return self.get_result_set_for_year(tz.now().year)

  # def get_survey_years(self):
  #   years = []
  #   for rs in self.resultset_set.all():
  #      years.append(rs.year)
  #   return years

  def __unicode__(self):
    return str(self.uid) + ", " + str(self.school)

  class Meta:
    db_table = u'Student'












class ResultSet(models.Model):
  load_kwargs = {'object_pairs_hook': collections.OrderedDict}
  student = models.ForeignKey(Student, default=None)
  year = models.PositiveSmallIntegerField(default=tz.now().year)
  completed = models.BooleanField(default=False)
  p1 = JSONField(load_kwargs=load_kwargs)
  p2 = JSONField(load_kwargs=load_kwargs)
  p3 = JSONField(load_kwargs=load_kwargs)
  p4 = JSONField(load_kwargs=load_kwargs)
  p5 = JSONField(load_kwargs=load_kwargs)
  p6 = JSONField(load_kwargs=load_kwargs)
  p7 = JSONField(load_kwargs=load_kwargs)
  p8 = JSONField(load_kwargs=load_kwargs)
  p9 = JSONField(load_kwargs=load_kwargs)
  p10 = JSONField(load_kwargs=load_kwargs)
  p11 = JSONField(load_kwargs=load_kwargs)

  # returns the percentage of students that answered each choice for the question
  # out of all other students in the school
  def get_q_percentage(self, page_num, q_num):
    choices = questions_page_choices[str(page_num)]['q'+str(q_num)]
    print choices

  # returns Boolean - true if all answers on page are NOT None
  def all_questions_answered(self, page_num):
    from .forms.questions_page_1 import skips as Page1Skips
    from .forms.questions_page_2 import skips as Page2Skips
    from .forms.questions_page_3 import skips as Page3Skips
    from .forms.questions_page_4 import skips as Page4Skips
    from .forms.questions_page_5 import skips as Page5Skips
    from .forms.questions_page_6 import skips as Page6Skips
    from .forms.questions_page_7 import skips as Page7Skips
    from .forms.questions_page_8 import skips as Page8Skips
    from .forms.questions_page_9 import skips as Page9Skips
    from .forms.questions_page_10 import skips as Page10Skips
    from .forms.questions_page_11 import skips as Page11Skips

    skips = {
      '1': Page1Skips,
      '2': Page2Skips,
      '3': Page3Skips,
      '4': Page4Skips,
      '5': Page5Skips,
      '6': Page6Skips,
      '7': Page7Skips,
      '8': Page8Skips,
      '9': Page9Skips,
      '10': Page10Skips,
      '11': Page11Skips
    }

    page_res_set = json.loads(getattr(self, 'p'+str(page_num)))
    all_questions_answered = True
    actual_skipped_questions = []
    skipped_questions_possible = []
    for cond in skips[str(page_num)].keys():
      for q in skips[str(page_num)][cond]:
        if q not in skipped_questions_possible:
          skipped_questions_possible.append(q)
    for q_num in range(1, num_questions_on_page[str(page_num)]+1):
      if page_res_set['q'+str(q_num)] == None or page_res_set['q'+str(q_num)] == '':
        actual_skipped_questions.append('p'+str(page_num)+'q'+str(q_num))
    for q in actual_skipped_questions:
      if q not in skipped_questions_possible:
        all_questions_answered = False
    return all_questions_answered

  def __unicode__(self):
    return 'ResultSet: id: ' + str(self.id)

  class Meta:
    db_table = 'ResultSet'

