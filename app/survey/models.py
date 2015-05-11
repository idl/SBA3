import hashlib
import collections
from django.db import models
from jsonfield import JSONField

class SchoolManager(models.Manager):
  def has_uid(self, uid):
    students = Student.objects.filter(school=self.model)
    print students

class School(models.Model):
  name = models.CharField(max_length=75, blank=False)
  location = models.CharField(max_length=125, help_text='Please enter the city and state of your school.')
  survey_title = models.CharField(max_length=50, null=True)
  date_created = models.DateField()

  objects = SchoolManager()

  def get_survey_years(self):
    print 'THIS SURVEY: ', self.name

  def __unicode__(self):
    return self.name

  class Meta:
    db_table = u'School'



# class UidManager(models.Manager):
#   def has_uid(self, uid):
#     students = Student.obj

# 1 Uid can have many Students
class Uid(models.Model):
  uid = models.CharField(max_length=20)

  def __unicode__(self):
    return self.uid

  class Meta:
    db_table = u'Uid'



# class ResultSetManager(models.Manager):
#   # return the percentage same for every question across all schools
#   def overall_percentage_all(self, uid):
#     try:
#       completed = Student.objects.values_list('completed', flat=True).filter(id=uid).get()
#       if not completed:
#         return 'Student has not completed the survey'
#     except:
#       return 'Student ID is not in the database'

#     percent_list = {}

#     for page in range(1, 12):
#       for question in range(1, 15):
#         question_id = 'p' + str(page) + 'q' + str(question)

#         try:
#           answer_list = self.values_list(question_id).filter(uid__completed=True)
#         except:
#           #return 'Question ID is not in the database'
#           continue

#         try:
#           student_answer = answer_list.filter(uid=uid).get()
#         except:
#           return 'No Answer for that Student ID'

#         student_total = 0.0
#         total_answers = 0.0
#         for answer in answer_list:
#           if answer == student_answer:
#             student_total += 1
#             total_answers += 1

#         percent_list[question_id] = student_total / total_answers

#     return percent_list

#   # return the percentage same for every question across participant's school
#   def school_percentage_all(self, uid):
#     try:
#       student = Student.objects.values('completed', 'school').filter(id=uid).get()
#       if not student['completed']:
#         return 'Student has not completed the survey'
#     except:
#       return 'Student ID is not in the database'

#     try:
#       school_list = Student.objects.values_list('id', flat=True).filter(school=student['school'], completed=True)
#     except:
#       return 'School ID is not in database'

#     percent_list = {}

#     for page in range(1, 12):
#       for question in range(1, 15):
#         question_id = 'p' + str(page) + 'q' + str(question)

#         try:
#           answer_list = self.values_list(question_id).filter(uid__in=school_list)
#         except:
#           # return 'Question ID is not in the database'
#           continue

#         try:
#           student_answer = answer_list.filter(uid=uid).get()
#         except:
#           return 'No Answer for that Student ID'

#         student_total = 0.0
#         total_answers = 0.0
#         for answer in answer_list:
#           if answer == student_answer:
#             student_total += 1
#           total_answers += 1

#         percent_list[question_id] = student_total / total_answers

#     return percent_list

#   # return the percentage same for given question across all schools
#   def overall_percentage_question(self, uid, question_id):
#     try:
#       completed = Student.objects.values_list('completed', flat=True).filter(id=uid).get()
#       if not completed:
#         return 'Student has not completed the survey'
#     except:
#       return 'Student ID is not in the database'

#     try:
#       answer_list = self.values_list(question_id).filter(uid__completed=True)
#     except:
#       return 'Question ID is not in the database'

#     try:
#       student_answer = answer_list.filter(uid=uid).get()
#     except:
#       return 'No Answer for that Student ID'

#     student_total = 0.0
#     total_answers = 0.0
#     for answer in answer_list:
#       if answer == student_answer:
#         student_total += 1
#       total_answers += 1

#     return student_total / total_answers

#   # return the percentage same for given question across participant's school
#   def school_percentage_question(self, uid, question_id):
#     try:
#       student = Student.objects.values('completed', 'school').filter(id=uid).get()
#       if not student['completed']:
#         return 'Student has not completed the survey'
#     except:
#       return 'Student ID is not in the database'

#     try:
#       school_list = Student.objects.values_list('id', flat=True).filter(school=student['school'], completed=True)
#     except:
#       return 'School ID is not in database'

#     try:
#       answer_list = self.values_list(question_id).filter(uid__in=school_list)
#     except:
#       return 'Question ID is not in the database'

#     try:
#       student_answer = answer_list.filter(uid=uid).get()
#     except:
#       return 'No Answer for that Student ID'

#     student_total = 0.0
#     total_answers = 0.0
#     for answer in answer_list:
#       if answer == student_answer:
#         student_total += 1
#       total_answers += 1

#     return student_total / total_answers

class ResultSet(models.Model):
  load_kwargs = {'object_pairs_hook': collections.OrderedDict}
  p1 = JSONField(load_kwargs=load_kwargs, null=True)
  p2 = JSONField(load_kwargs=load_kwargs, null=True)
  p3 = JSONField(load_kwargs=load_kwargs, null=True)
  p4 = JSONField(load_kwargs=load_kwargs, null=True)
  p5 = JSONField(load_kwargs=load_kwargs, null=True)
  p6 = JSONField(load_kwargs=load_kwargs, null=True)
  p7 = JSONField(load_kwargs=load_kwargs, null=True)
  p8 = JSONField(load_kwargs=load_kwargs, null=True)
  p9 = JSONField(load_kwargs=load_kwargs, null=True)
  p10 = JSONField(load_kwargs=load_kwargs, null=True)
  p11 = JSONField(load_kwargs=load_kwargs, null=True)

  # objects = ResultSetManager()

  def __unicode__(self):
    return 'ResultSet: ' + str(self.id)

  class Meta:
    db_table = 'ResultSet'






class StudentManager(models.Manager):
  def create_student(self, uid, school):
    error = ''
    if not uid:
      error = 'Student must have a uid'
    elif not school:
      error = 'Student must have a school'

    if Student.objects.filter(uid__iexact=uid, school=school).count() > 0:
      error = 'Student - School association already exists'
    else:
      continue_hash = hashlib.sha256(uid + school.name).hexdigest()
      continue_pass = continue_hash[:10]

      student = self.model(
        uid=uid,
        school=school,
        continue_pass=continue_pass,
        completed=False
      ).save()

      return student
    if error == '':
      error = 'Unknown Error'
    return error


class Student(models.Model):
  school = models.ForeignKey(School)
  continue_pass = models.CharField(max_length=10, blank=False)
  completed = models.BooleanField()
  result_set = models.OneToOneField(ResultSet, null=True)
  uid = models.ForeignKey(Uid) # 1 Uid -> n Students (multiple
                               # students fromdifferent schools can have the
                               #  same school Uid)
  objects = StudentManager()

  def has_started_survey(self):
    if self.result_set_id is None or self.result_set is None or self.result_set.p1 is None:
      return False
    else:
      return True

  def __unicode__(self):
    return str(self.uid) + ", " + str(self.school)

  class Meta:
    db_table = u'Student'





