from django.db import models
from .settings import AUTH_USER_MODEL

import hashlib

class School(models.Model):
    name = models.CharField(max_length=75, blank=False)
    location = models.CharField(max_length=125, help_text='Please enter the city and state of your school.')
    # user = models.OneToOneField(AUTH_USER_MODEL)
    
    def __unicode__(self):
        return self.name

    # def create_school(self, name, email, location, user_id):
    #     if not name:
    #         raise ValueError("School must have a name")
    #     elif not email:
    #         raise ValueError("School must have a contact email")
    #     elif not location:
    #         raise ValueError("School must have a location")
    #     elif not user_id:
    #         raise ValueError("School must have an admin user")
    #     email = self.normalize_email(email)
    #     school = self.model(
    #                             name = name,
    #                             email = email,
    #                             location = location,
    #                             user = user_id
    #                         )
    #     school.save(using=self._db)
    #     return school

class StudentManager(models.Manager):
    def create_student(self, user_id, school_id):
        if not user_id:
            raise ValueError("Student must have a user_id")
        elif not school_id:
            raise ValueError("Student must have a school")

        if Student.objects.filter(user_id=user_id).count() != 0:
            student = Student.objects.filter(user_id=user_id).get()
            if student.school_id == school_id:
                raise ValueError({'error':'Student - School association already exists'})
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
        return None

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
    p1q1 = models.CharField(max_length=20)
    p1q2 = models.CharField(max_length=20)
    p1q3 = models.CharField(max_length=20)
    p1q4 = models.CharField(max_length=20)
    p1q5 = models.CharField(max_length=20)
    p1q6 = models.CharField(max_length=20)
    p1q7 = models.CharField(max_length=20)
    p1q8 = models.CharField(max_length=20)
    p1q9 = models.CharField(max_length=20)
    p1q10 = models.CharField(max_length=20)
    p1q11 = models.CharField(max_length=20)
    p2q1 = models.CharField(max_length=20)
    p2q2 = models.CharField(max_length=20)
    p2q3 = models.CharField(max_length=20)
    p2q4 = models.CharField(max_length=20)
    p2q5 = models.CharField(max_length=20)
    p2q6 = models.CharField(max_length=20)
    p2q7 = models.CharField(max_length=20)
    p2q8 = models.CharField(max_length=20)
    p2q9 = models.CharField(max_length=20)
    p2q10 = models.CharField(max_length=20)
    p2q11 = models.CharField(max_length=20)
    p3q1 = models.CharField(max_length=20)
    p3q2 = models.CharField(max_length=20)
    p3q3 = models.CharField(max_length=20)
    p3q4 = models.CharField(max_length=20)
    p3q5 = models.CharField(max_length=20)
    p3q6 = models.CharField(max_length=20)
    p3q7 = models.CharField(max_length=20)
    p3q8 = models.CharField(max_length=20)
    p3q9 = models.CharField(max_length=20)
    p4q1 = models.CharField(max_length=20)
    p4q2 = models.CharField(max_length=20)
    p4q3 = models.CharField(max_length=20)
    p4q4 = models.CharField(max_length=20)
    p4q5 = models.CharField(max_length=20)
    p4q6 = models.CharField(max_length=20)
    p4q7 = models.CharField(max_length=20)
    p4q8 = models.CharField(max_length=20)
    p4q9 = models.CharField(max_length=20)
    p4q10 = models.CharField(max_length=20)
    p4q11 = models.CharField(max_length=20)
    p5q1 = models.CharField(max_length=20)
    p5q2 = models.CharField(max_length=20)
    p5q3 = models.CharField(max_length=20)
    p5q4 = models.CharField(max_length=20)
    p5q5 = models.CharField(max_length=20)
    p5q6 = models.CharField(max_length=20)
    p5q7 = models.CharField(max_length=20)
    p5q8 = models.CharField(max_length=20)
    p5q9 = models.CharField(max_length=20)
    p5q10 = models.CharField(max_length=20)
    p5q11 = models.CharField(max_length=20)
    p5q12 = models.CharField(max_length=20)
    p5q13 = models.CharField(max_length=20)
    p5q14 = models.CharField(max_length=20)
    p6q1 = models.CharField(max_length=20)
    p6q2 = models.CharField(max_length=20)
    p6q3 = models.CharField(max_length=20)
    p6q4 = models.CharField(max_length=20)
    p6q5 = models.CharField(max_length=20)
    p6q6 = models.CharField(max_length=20)
    p6q7 = models.CharField(max_length=20)
    p6q8 = models.CharField(max_length=20)
    p6q9 = models.CharField(max_length=20)
    p6q10 = models.CharField(max_length=20)
    p6q11 = models.CharField(max_length=20)
    p6q12 = models.CharField(max_length=20)
    p7q1 = models.CharField(max_length=20)
    p7q2 = models.CharField(max_length=20)
    p7q3 = models.CharField(max_length=20)
    p7q4 = models.CharField(max_length=20)
    p7q5 = models.CharField(max_length=20)
    p7q6 = models.CharField(max_length=20)
    p7q7 = models.CharField(max_length=20)
    p7q8 = models.CharField(max_length=20)
    p7q9 = models.CharField(max_length=20)
    p8q1 = models.CharField(max_length=20)
    p8q2 = models.CharField(max_length=20)
    p8q3 = models.CharField(max_length=20)
    p8q4 = models.CharField(max_length=20)
    p8q5 = models.CharField(max_length=20)
    p8q6 = models.CharField(max_length=20)
    p8q7 = models.CharField(max_length=20)
    p8q8 = models.CharField(max_length=20)
    p8q9 = models.CharField(max_length=20)
    p8q10 = models.CharField(max_length=20)
    p8q11 = models.CharField(max_length=20)
    p8q12 = models.CharField(max_length=20)
    p9q1 = models.CharField(max_length=20)
    p9q2 = models.CharField(max_length=20)
    p9q3 = models.CharField(max_length=20)
    p9q4 = models.CharField(max_length=20)
    p9q5 = models.CharField(max_length=20)
    p9q6 = models.CharField(max_length=20)
    p9q7 = models.CharField(max_length=20)
    p9q8 = models.CharField(max_length=20)
    p9q9 = models.CharField(max_length=20)
    p9q10 = models.CharField(max_length=20)
    p9q11 = models.CharField(max_length=20)
    p9q12 = models.CharField(max_length=20)
    p9q13 = models.CharField(max_length=20)
    p11q1 = models.CharField(max_length=20)
    p11q2 = models.CharField(max_length=20)
    p11q3 = models.CharField(max_length=20)
    p11q4 = models.CharField(max_length=20)
    p11q5 = models.CharField(max_length=20)
    p11q6 = models.CharField(max_length=20)
    p11q7 = models.CharField(max_length=20)
    p11q8 = models.CharField(max_length=20)
    p11q9 = models.CharField(max_length=20)
    p11q10 = models.CharField(max_length=20)
    p11q11 = models.CharField(max_length=20)
    p11q12 = models.CharField(max_length=20)
    p11q13 = models.CharField(max_length=20)
    p11q14 = models.CharField(max_length=20)

    def __unicode__(self):
    	return 'Answer Set'
