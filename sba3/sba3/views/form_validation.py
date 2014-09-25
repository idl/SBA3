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

        if school_id == '' and user_id == '':
            err_msg = 'School and Identifier fields cannot be blank.'
        elif school_id == '':
            err_msg = 'School field cannot be blank.'
        elif user_id == '':
            err_msg = 'Identifier field cannot be blank.'

        else:
            school = School.objects.filter(id=school_id).get()

            survey_form = surveyLoginForm(request.POST)
            if user_id and survey_form.is_valid():
                if Student.objects.filter(user_id=user_id, school_id=school).count() > 1:
                    request.session['user_id'] = user_id
                    request.session['school_id'] = school_id
                    return redirect('/#continue')
                else:
                    new_student = Student.objects.create_student(user_id, school)
                    if isinstance(new_student, str):
                        request.session['err_msg'] = new_student
                        return redirect('/#start')
                    else:
                        request.session['user_id'] = new_student.id
                        request.session['continue_pass'] = new_student.continue_pass
                        return redirect('page', 1)

        request.session['err_msg'] = err_msg
    return redirect('/#start')

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
            request.session['continue_err_msg'] = err_msg
            return redirect('/#continue')

        school = School.objects.filter(id=school_id).get()

        if Student.objects.filter(user_id=user_id, school_id=school, continue_pass=continue_pass).count() == 1:
            current_student = Student.objects.filter(user_id=user_id, school_id=school, continue_pass=continue_pass).get()
            if current_student.completed == False:
                request.session['continue_pass'] = continue_pass
                request.session['user_id'] = current_student.id
                try:
                    session_build = {}
                    current_answers = AnswerSet.objects.values().filter(student_id=current_student).get()
                    for answer in current_answers:
                        if current_answers[answer]:
                            if answer[0] == 'p':
                                if answer[2] == 'q':
                                    array_name = answer[:2]
                                    question_number = answer[3:]
                                elif answer[3]  == 'q':
                                    array_name = answer[:3]
                                    question_number = answer[4:]
                                else:
                                    array_name = ''
                                    question_number = ''

                                if array_name in session_build:
                                    session_build[array_name].update({question_number: current_answers[answer]})
                                else:
                                    session_build[array_name] = {question_number: current_answers[answer]}
       
                    print session_build
                    for array_name in session_build:
                        current = 1
                        temp_array = []
                        current_array = session_build[array_name]
                        for answer in current_array:
                            temp_array.append(current_array.get(str(current), ''))
                            current = current + 1
     
                        request.session[array_name] = temp_array

                        # rebuild session
                    return redirect('page', 11)
                except:
                    return redirect('page', 1)

    return redirect('/#continue')