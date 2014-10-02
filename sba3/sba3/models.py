from django.db import models
from .settings import AUTH_USER_MODEL
from django.utils import timezone as tz

import hashlib

class School(models.Model):
    name = models.CharField(max_length=75, blank=False)
    location = models.CharField(max_length=125, help_text='Please enter the city and state of your school.')
    date_created = models.CharField(default=tz.now(), editable=False, max_length=125)
    # user = models.OneToOneField(AUTH_USER_MODEL)
    
    def __unicode__(self):
        return self.name

class StudentManager(models.Manager):
    def create_student(self, user_id, school_id):
        error = ''
        if not user_id:
            error = "Student must have a user_id"
        elif not school_id:
            error = "Student must have a school"

        if Student.objects.filter(user_id=user_id).count() != 0:
            student = Student.objects.filter(user_id=user_id).get()
            if student.school_id == school_id:
                error = 'Student - School association already exists'
        else:
            school = School.objects.filter(pk=1).get()

            continue_hash = hashlib.sha256(user_id + school.name).hexdigest()
            continue_pass = continue_hash[:10]

            student = self.model(
                                    user_id=user_id,
                                    school_id=school,
                                    continue_pass=continue_pass,
                                    completed=False
                                )
            student.save()

            return student
        if error == '':
            error = 'Unknown Error'
        return error

class Student(models.Model):
    user_id = models.CharField(max_length=10, db_index = True)
    school_id = models.ForeignKey(School, null=True)
    continue_pass = models.CharField(max_length=10, blank=False)
    completed = models.BooleanField()

    objects = StudentManager()

    def __unicode__(self):
        return self.user_id


class AnswerSet(models.Model):
    student_id = models.ForeignKey(Student, db_index = True)
    p1q1 = models.CharField(max_length=20, null=True)
    p1q2 = models.CharField(max_length=20, null=True)
    p1q3 = models.CharField(max_length=20, null=True)
    p1q4 = models.CharField(max_length=20, null=True)
    p1q5 = models.CharField(max_length=20, null=True)
    p1q6 = models.CharField(max_length=20, null=True)
    p1q7 = models.CharField(max_length=20, null=True)
    p1q8 = models.CharField(max_length=20, null=True)
    p1q9 = models.CharField(max_length=20, null=True)
    p1q10 = models.CharField(max_length=20, null=True)
    p1q11 = models.CharField(max_length=20, null=True)
    p2q1 = models.CharField(max_length=20, null=True)
    p2q2 = models.CharField(max_length=20, null=True)
    p2q3 = models.CharField(max_length=20, null=True)
    p2q4 = models.CharField(max_length=20, null=True)
    p2q5 = models.CharField(max_length=20, null=True)
    p2q6 = models.CharField(max_length=20, null=True)
    p2q7 = models.CharField(max_length=20, null=True)
    p2q8 = models.CharField(max_length=20, null=True)
    p2q9 = models.CharField(max_length=20, null=True)
    p2q10 = models.CharField(max_length=20, null=True)
    p2q11 = models.CharField(max_length=20, null=True)
    p3q1 = models.CharField(max_length=20, null=True)
    p3q2 = models.CharField(max_length=20, null=True)
    p3q3 = models.CharField(max_length=20, null=True)
    p3q4 = models.CharField(max_length=20, null=True)
    p3q5 = models.CharField(max_length=20, null=True)
    p3q6 = models.CharField(max_length=20, null=True)
    p3q7 = models.CharField(max_length=20, null=True)
    p3q8 = models.CharField(max_length=20, null=True)
    p3q9 = models.CharField(max_length=20, null=True)
    p4q1 = models.CharField(max_length=20, null=True)
    p4q2 = models.CharField(max_length=20, null=True)
    p4q3 = models.CharField(max_length=20, null=True)
    p4q4 = models.CharField(max_length=20, null=True)
    p4q5 = models.CharField(max_length=20, null=True)
    p4q6 = models.CharField(max_length=20, null=True)
    p4q7 = models.CharField(max_length=20, null=True)
    p4q8 = models.CharField(max_length=20, null=True)
    p4q9 = models.CharField(max_length=20, null=True)
    p4q10 = models.CharField(max_length=20, null=True)
    p4q11 = models.CharField(max_length=20, null=True)
    p5q1 = models.CharField(max_length=20, null=True)
    p5q2 = models.CharField(max_length=20, null=True)
    p5q3 = models.CharField(max_length=20, null=True)
    p5q4 = models.CharField(max_length=20, null=True)
    p5q5 = models.CharField(max_length=20, null=True)
    p5q6 = models.CharField(max_length=20, null=True)
    p5q7 = models.CharField(max_length=20, null=True)
    p5q8 = models.CharField(max_length=20, null=True)
    p5q9 = models.CharField(max_length=20, null=True)
    p5q10 = models.CharField(max_length=20, null=True)
    p5q11 = models.CharField(max_length=20, null=True)
    p5q12 = models.CharField(max_length=20, null=True)
    p5q13 = models.CharField(max_length=20, null=True)
    p5q14 = models.CharField(max_length=20, null=True)
    p6q1 = models.CharField(max_length=20, null=True)
    p6q2 = models.CharField(max_length=20, null=True)
    p6q3 = models.CharField(max_length=20, null=True)
    p6q4 = models.CharField(max_length=20, null=True)
    p6q5 = models.CharField(max_length=20, null=True)
    p6q6 = models.CharField(max_length=20, null=True)
    p6q7 = models.CharField(max_length=20, null=True)
    p6q8 = models.CharField(max_length=20, null=True)
    p6q9 = models.CharField(max_length=20, null=True)
    p6q10 = models.CharField(max_length=20, null=True)
    p6q11 = models.CharField(max_length=20, null=True)
    p6q12 = models.CharField(max_length=20, null=True)
    p7q1 = models.CharField(max_length=20, null=True)
    p7q2 = models.CharField(max_length=20, null=True)
    p7q3 = models.CharField(max_length=20, null=True)
    p7q4 = models.CharField(max_length=20, null=True)
    p7q5 = models.CharField(max_length=20, null=True)
    p7q6 = models.CharField(max_length=20, null=True)
    p7q7 = models.CharField(max_length=20, null=True)
    p7q8 = models.CharField(max_length=20, null=True)
    p7q9 = models.CharField(max_length=20, null=True)
    p8q1 = models.CharField(max_length=20, null=True)
    p8q2 = models.CharField(max_length=20, null=True)
    p8q3 = models.CharField(max_length=20, null=True)
    p8q4 = models.CharField(max_length=20, null=True)
    p8q5 = models.CharField(max_length=20, null=True)
    p8q6 = models.CharField(max_length=20, null=True)
    p8q7 = models.CharField(max_length=20, null=True)
    p8q8 = models.CharField(max_length=20, null=True)
    p8q9 = models.CharField(max_length=20, null=True)
    p8q10 = models.CharField(max_length=20, null=True)
    p8q11 = models.CharField(max_length=20, null=True)
    p8q12 = models.CharField(max_length=20, null=True)
    p9q1 = models.CharField(max_length=20, null=True)
    p9q2 = models.CharField(max_length=20, null=True)
    p9q3 = models.CharField(max_length=20, null=True)
    p9q4 = models.CharField(max_length=20, null=True)
    p9q5 = models.CharField(max_length=20, null=True)
    p9q6 = models.CharField(max_length=20, null=True)
    p9q7 = models.CharField(max_length=20, null=True)
    p9q8 = models.CharField(max_length=20, null=True)
    p9q9 = models.CharField(max_length=20, null=True)
    p9q10 = models.CharField(max_length=20, null=True)
    p9q11 = models.CharField(max_length=20, null=True)
    p9q12 = models.CharField(max_length=20, null=True)
    p9q13 = models.CharField(max_length=20, null=True)
    p11q1 = models.CharField(max_length=20, null=True)
    p11q2 = models.CharField(max_length=20, null=True)
    p11q3 = models.CharField(max_length=20, null=True)
    p11q4 = models.CharField(max_length=20, null=True)
    p11q5 = models.CharField(max_length=20, null=True)
    p11q6 = models.CharField(max_length=20, null=True)
    p11q7 = models.CharField(max_length=20, null=True)
    p11q8 = models.CharField(max_length=20, null=True)
    p11q9 = models.CharField(max_length=20, null=True)
    p11q10 = models.CharField(max_length=20, null=True)
    p11q11 = models.CharField(max_length=20, null=True)
    p11q12 = models.CharField(max_length=20, null=True)
    p11q13 = models.CharField(max_length=20, null=True)
    p11q14 = models.CharField(max_length=20, null=True)

    def __unicode__(self):
    	return 'Answer Set'
