from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.loading import get_model

from ..forms import surveyLoginForm
from admin_custom.forms import LoginForm
from ..models import Student, School, AnswerSet

def start_survey(request):
    if request.POST:
        school_id = request.POST.get('school', '')
        user_id = request.POST.get('identifier', '')

        school = School.objects.filter(id=school_id).get()

        survey_form = surveyLoginForm(request.POST)
        if user_id and survey_form.is_valid():
            if Student.objects.filter(user_id=user_id, school_id=school).count() > 1:
                request.session['user_id'] = user_id
                request.session['school_id'] = school_id
                return redirect('/#continue')
            else:
                try:
                    new_student = Student.objects.create_student(user_id, school)
                    request.session['user_id'] = new_student.id
                    request.session['continue_pass'] = new_student.continue_pass
                    return redirect('page', 1)
                except ValueError, e:
                    request.session['err_msg'] = e
                    return redirect('/#survey')
        else:
            if school_id == '' and user_id == '':
                err_msg = 'School and Identifier fields cannot be blank.'
            elif school_id == '':
                err_msg = 'School field cannot be blank.'
            elif user_id == '':
                err_msg = 'Identifier field cannot be blank.'
            request.session['err_msg'] = err_msg
    return redirect('/#survey')

def continue_survey(request):
    if request.POST:
        continue_pass = request.POST.get('passkey', '')
        user_id = request.POST.get('identifier', '')
        school_id = request.POST.get('school', '')

        print continue_pass
        print user_id
        print school_id

        if school_id == '' or user_id == '' or continue_pass == '':
            err_msg = 'School, Identifier, and Passkey fields cannot be blank.'
            request.session['err_msg'] = err_msg
            return redirect('/#continue')

        school = School.objects.filter(id=school_id).get()

        if Student.objects.filter(user_id=user_id, school_id=school, continue_pass=continue_pass).count() == 1:
            current_student = Student.objects.filter(user_id=user_id, school_id=school, continue_pass=continue_pass).get()
            if current_student.completed == False:
                request.session['continue_pass'] = continue_pass
                request.session['user_id'] = current_student.id
                try:
                    current_answers = AnswerSet.objects.values().filter(student_id=current_student)
                    for answer in current_answers:
                        print answer
                        # rebuild session
                    return redirect('page', 1)
                except:
                    return redirect('page', 1)

    return redirect('/#continue')