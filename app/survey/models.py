import hashlib
from django.db import models
from django.contrib.postgres.fields import ArrayField


class School(models.Model):
  name = models.CharField(max_length=75, blank=False)
  location = models.CharField(max_length=125, help_text='Please enter the city and state of your school.')
  survey_title = models.CharField(max_length=50, null=True)
  date = models.DateField()

  def get_survey_years(self):
    print 'THIS SURVEY: ', self.name

  def __unicode__(self):
    return self.name

  class Meta:
    db_table = 'School'



# class SchoolUidManager(models.Manager):
#   def check_uid(self, school, uid):
#     if SchoolUid.objects.filter(school_id=school, uid=uid).count == 1:
#       return True
#     else:
#       return False

# class SchoolUid(models.Model):
#   school_id = models.ForeignKey(School)
#   uid = models.CharField(max_length=20)

#   objects = SchoolUidManager()



# class StudentManager(models.Manager):
#   def create_student(self, user_id, school):
#     error = ''
#     if not user_id:
#       error = 'Student must have a user_id'
#     elif not school:
#       error = 'Student must have a school'

#     if Student.objects.filter(user_id__iexact=user_id, school_id=school).count() != 0:
#       error = 'Student - School association already exists'
#     else:
#       continue_hash = hashlib.sha256(user_id + school.name).hexdigest()
#       continue_pass = continue_hash[:10]

#       student = self.model(
#         user_id=user_id,
#         school_id=school,
#         continue_pass=continue_pass,
#         completed=False
#       )
#       student.save()

#       return student
#     if error == '':
#       error = 'Unknown Error'
#     return error

# class Student(models.Model):
#   user_id = models.CharField(max_length=20)
#   school_id = models.ForeignKey(School, null=True)
#   continue_pass = models.CharField(max_length=10, blank=False)
#   completed = models.BooleanField()

#   objects = StudentManager()

#   class Meta:
#     db_table = 'Student'



# class ResultSetManager(models.Manager):
#   # return the percentage same for every question across all schools
#   def overall_percentage_all(self, student_id):
#     try:
#       completed = Student.objects.values_list('completed', flat=True).filter(id=student_id).get()
#       if not completed:
#         return 'Student has not completed the survey'
#     except:
#       return 'Student ID is not in the database'

#     percent_list = {}

#     for page in range(1, 12):
#       for question in range(1, 15):
#         question_id = 'p' + str(page) + 'q' + str(question)

#         try:
#           answer_list = self.values_list(question_id).filter(student_id__completed=True)
#         except:
#           #return 'Question ID is not in the database'
#           continue

#         try:
#           student_answer = answer_list.filter(student_id=student_id).get()
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
#   def school_percentage_all(self, student_id):
#     try:
#       student = Student.objects.values('completed', 'school_id').filter(id=student_id).get()
#       if not student['completed']:
#         return 'Student has not completed the survey'
#     except:
#       return 'Student ID is not in the database'

#     try:
#       school_list = Student.objects.values_list('id', flat=True).filter(school_id=student['school_id'], completed=True)
#     except:
#       return 'School ID is not in database'

#     percent_list = {}

#     for page in range(1, 12):
#       for question in range(1, 15):
#         question_id = 'p' + str(page) + 'q' + str(question)

#         try:
#           answer_list = self.values_list(question_id).filter(student_id__in=school_list)
#         except:
#           # return 'Question ID is not in the database'
#           continue

#         try:
#           student_answer = answer_list.filter(student_id=student_id).get()
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
#   def overall_percentage_question(self, student_id, question_id):
#     try:
#       completed = Student.objects.values_list('completed', flat=True).filter(id=student_id).get()
#       if not completed:
#         return 'Student has not completed the survey'
#     except:
#       return 'Student ID is not in the database'

#     try:
#       answer_list = self.values_list(question_id).filter(student_id__completed=True)
#     except:
#       return 'Question ID is not in the database'

#     try:
#       student_answer = answer_list.filter(student_id=student_id).get()
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
#   def school_percentage_question(self, student_id, question_id):
#     try:
#       student = Student.objects.values('completed', 'school_id').filter(id=student_id).get()
#       if not student['completed']:
#         return 'Student has not completed the survey'
#     except:
#       return 'Student ID is not in the database'

#     try:
#       school_list = Student.objects.values_list('id', flat=True).filter(school_id=student['school_id'], completed=True)
#     except:
#       return 'School ID is not in database'

#     try:
#       answer_list = self.values_list(question_id).filter(student_id__in=school_list)
#     except:
#       return 'Question ID is not in the database'

#     try:
#       student_answer = answer_list.filter(student_id=student_id).get()
#     except:
#       return 'No Answer for that Student ID'

#     student_total = 0.0
#     total_answers = 0.0
#     for answer in answer_list:
#       if answer == student_answer:
#         student_total += 1
#       total_answers += 1

#     return student_total / total_answers

# class ResultSet(models.Model):
#   student_id = models.ForeignKey(Student, db_index = True)
#   p1q1 = models.CharField(max_length=20, null=True)
#   p1q2 = models.CharField(max_length=20, null=True)
#   p1q3 = models.CharField(max_length=20, null=True)
#   p1q4 = models.CharField(max_length=20, null=True)
#   p1q5 = models.CharField(max_length=20, null=True)
#   p1q6 = models.CharField(max_length=20, null=True)
#   p1q7 = models.CharField(max_length=20, null=True)
#   p1q8 = models.CharField(max_length=20, null=True)
#   p1q9 = models.CharField(max_length=20, null=True)
#   p1q10 = models.CharField(max_length=20, null=True)
#   p1q11 = models.CharField(max_length=20, null=True)
#   p2q1 = models.CharField(max_length=20, null=True)
#   p2q2 = models.CharField(max_length=20, null=True)
#   p2q3 = models.CharField(max_length=20, null=True)
#   p2q4 = models.CharField(max_length=20, null=True)
#   p2q5 = models.CharField(max_length=20, null=True)
#   p2q6 = models.CharField(max_length=20, null=True)
#   p2q7 = models.CharField(max_length=20, null=True)
#   p2q8 = models.CharField(max_length=20, null=True)
#   p2q9 = models.CharField(max_length=20, null=True)
#   p2q10 = models.CharField(max_length=20, null=True)
#   p2q11 = models.CharField(max_length=20, null=True)
#   p3q1 = models.CharField(max_length=20, null=True)
#   p3q2 = models.CharField(max_length=20, null=True)
#   p3q3 = models.CharField(max_length=20, null=True)
#   p3q4 = models.CharField(max_length=20, null=True)
#   p3q5 = models.CharField(max_length=20, null=True)
#   p3q6 = models.CharField(max_length=20, null=True)
#   p3q7 = models.CharField(max_length=20, null=True)
#   p3q8 = models.CharField(max_length=20, null=True)
#   p3q9 = models.CharField(max_length=20, null=True)
#   p4q1 = models.CharField(max_length=20, null=True)
#   p4q2 = models.CharField(max_length=20, null=True)
#   p4q3 = models.CharField(max_length=20, null=True)
#   p4q4 = models.CharField(max_length=20, null=True)
#   p4q5 = models.CharField(max_length=20, null=True)
#   p4q6 = models.CharField(max_length=20, null=True)
#   p4q7 = models.CharField(max_length=20, null=True)
#   p4q8 = models.CharField(max_length=20, null=True)
#   p4q9 = models.CharField(max_length=20, null=True)
#   p4q10 = models.CharField(max_length=20, null=True)
#   p4q11 = models.CharField(max_length=20, null=True)
#   p5q1 = models.CharField(max_length=20, null=True)
#   p5q2 = models.CharField(max_length=20, null=True)
#   p5q3 = models.CharField(max_length=20, null=True)
#   p5q4 = models.CharField(max_length=20, null=True)
#   p5q5 = models.CharField(max_length=20, null=True)
#   p5q6 = models.CharField(max_length=20, null=True)
#   p5q7 = models.CharField(max_length=20, null=True)
#   p5q8 = models.CharField(max_length=20, null=True)
#   p5q9 = models.CharField(max_length=20, null=True)
#   p5q10 = models.CharField(max_length=20, null=True)
#   p5q11 = models.CharField(max_length=20, null=True)
#   p5q12 = models.CharField(max_length=20, null=True)
#   p5q13 = models.CharField(max_length=20, null=True)
#   p5q14 = models.CharField(max_length=20, null=True)
#   p6q1 = models.CharField(max_length=20, null=True)
#   p6q2 = models.CharField(max_length=20, null=True)
#   p6q3 = models.CharField(max_length=20, null=True)
#   p6q4 = models.CharField(max_length=20, null=True)
#   p6q5 = models.CharField(max_length=20, null=True)
#   p6q6 = models.CharField(max_length=20, null=True)
#   p6q7 = models.CharField(max_length=20, null=True)
#   p6q8 = models.CharField(max_length=20, null=True)
#   p6q9 = models.CharField(max_length=20, null=True)
#   p6q10 = models.CharField(max_length=20, null=True)
#   p6q11 = models.CharField(max_length=20, null=True)
#   p6q12 = models.CharField(max_length=20, null=True)
#   p7q1 = models.CharField(max_length=20, null=True)
#   p7q2 = models.CharField(max_length=20, null=True)
#   p7q3 = models.CharField(max_length=20, null=True)
#   p7q4 = models.CharField(max_length=20, null=True)
#   p7q5 = models.CharField(max_length=20, null=True)
#   p7q6 = models.CharField(max_length=20, null=True)
#   p7q7 = models.CharField(max_length=20, null=True)
#   p7q8 = models.CharField(max_length=20, null=True)
#   p7q9 = models.CharField(max_length=20, null=True)
#   p8q1 = models.CharField(max_length=20, null=True)
#   p8q2 = models.CharField(max_length=20, null=True)
#   p8q3 = models.CharField(max_length=20, null=True)
#   p8q4 = models.CharField(max_length=20, null=True)
#   p8q5 = models.CharField(max_length=20, null=True)
#   p8q6 = models.CharField(max_length=20, null=True)
#   p8q7 = models.CharField(max_length=20, null=True)
#   p8q8 = models.CharField(max_length=20, null=True)
#   p8q9 = models.CharField(max_length=20, null=True)
#   p8q10 = models.CharField(max_length=20, null=True)
#   p8q11 = models.CharField(max_length=20, null=True)
#   p8q12 = models.CharField(max_length=20, null=True)
#   p9q1 = models.CharField(max_length=20, null=True)
#   p9q2 = models.CharField(max_length=20, null=True)
#   p9q3 = models.CharField(max_length=20, null=True)
#   p9q4 = models.CharField(max_length=20, null=True)
#   p9q5 = models.CharField(max_length=20, null=True)
#   p9q6 = models.CharField(max_length=20, null=True)
#   p9q7 = models.CharField(max_length=20, null=True)
#   p9q8 = models.CharField(max_length=20, null=True)
#   p9q9 = models.CharField(max_length=20, null=True)
#   p9q10 = models.CharField(max_length=20, null=True)
#   p9q11 = models.CharField(max_length=20, null=True)
#   p9q12 = models.CharField(max_length=20, null=True)
#   p9q13 = models.CharField(max_length=20, null=True)
#   p10q1 = models.CharField(max_length=2, null=True)
#   p10q2 = models.CharField(max_length=2, null=True)
#   p10q3 = models.CharField(max_length=2, null=True)
#   p10q4 = models.CharField(max_length=2, null=True)
#   p10q5 = models.CharField(max_length=2, null=True)
#   p10q6 = models.CharField(max_length=2, null=True)
#   p10q7 = models.TextField(max_length=255, null=True)
#   p10q8 = models.TextField(max_length=255, null=True)
#   p10q9 = models.TextField(max_length=255, null=True)
#   p10q10 = models.TextField(max_length=255, null=True)
#   p10q11 = models.TextField(max_length=255, null=True)
#   p10q12 = models.TextField(max_length=255, null=True)
#   p11q1 = models.CharField(max_length=20, null=True)
#   p11q2 = models.CharField(max_length=20, null=True)
#   p11q3 = models.CharField(max_length=20, null=True)
#   p11q4 = models.CharField(max_length=20, null=True)
#   p11q5 = models.CharField(max_length=20, null=True)
#   p11q6 = models.CharField(max_length=20, null=True)
#   p11q7 = models.CharField(max_length=20, null=True)
#   p11q8 = models.CharField(max_length=20, null=True)
#   p11q9 = models.CharField(max_length=20, null=True)
#   p11q10 = models.CharField(max_length=20, null=True)
#   p11q11 = models.CharField(max_length=20, null=True)
#   p11q12 = models.CharField(max_length=20, null=True)
#   p11q13 = models.CharField(max_length=20, null=True)
#   p11q14 = models.CharField(max_length=20, null=True)

#   objects = ResultSetManager()

#   def __unicode__(self):
#     return 'Answer Set'

#   class Meta:
#     db_table = 'SurveyResultSet'
