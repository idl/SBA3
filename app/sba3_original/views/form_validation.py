from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.loading import get_model

from ..forms import surveyLoginForm
from admin_custom.forms import LoginForm
from ..models import Student, School, AnswerSet, SchoolUid

def start_survey(request):
    if request.POST:
        school_id = request.POST.get('school', '')
        survey_user_id = request.POST.get('identifier', '')

        if school_id == '' and survey_user_id == '':
            err_msg = 'School and Identifier fields cannot be blank.'
        elif school_id == '':
            err_msg = 'School field cannot be blank.'
        elif survey_user_id == '':
            err_msg = 'Identifier field cannot be blank.'

        else:
            school = School.objects.filter(id=school_id).get()

            survey_form = surveyLoginForm(request.POST)

            if survey_user_id and survey_form.is_valid():
                uid_list = SchoolUid.objects.values_list('uid', flat=True).filter(school_id=school_id)
                if uid_list:
                    if survey_user_id in uid_list:
                        new_student = Student.objects.create_student(survey_user_id, school)
                    else:
                        new_student = str(survey_user_id) + ' is not registerd a registered user id with ' + str(school.name)
                else:
                    new_student = Student.objects.create_student(survey_user_id, school)

                if isinstance(new_student, str):
                    request.session['err_msg'] = new_student
                    return redirect('/#start')
                else:
                    request.session['survey_user_id'] = new_student.id
                    request.session['continue_pass'] = new_student.continue_pass
                    request.session['survey_title'] = school.survey_title
                    return redirect('page', 1)

        request.session['err_msg'] = err_msg
    return redirect('/#start')

def continue_survey(request):
    if request.POST:
        continue_pass = request.POST.get('passkey', '')
        survey_user_id = request.POST.get('identifier', '')
        school_id = request.POST.get('school', '')


        if school_id == '' or survey_user_id == '' or continue_pass == '':
            err_msg = 'School, Identifier, and Passkey fields cannot be blank.'
            request.session['continue_err_msg'] = err_msg
            return redirect('/#continue')

        school = School.objects.filter(id=school_id).get()


        if Student.objects.filter(user_id__iexact=survey_user_id, school_id=school, continue_pass=continue_pass).count() == 1:
            current_student = Student.objects.filter(user_id=survey_user_id, school_id=school, continue_pass=continue_pass).get()
            if current_student.completed == False:
                request.session['continue_pass'] = continue_pass
                request.session['survey_user_id'] = current_student.id
                request.session['survey_title'] = school.survey_title

                try:
                    session_build = {}
                    current_answers = AnswerSet.objects.values().filter(student_id=current_student).get()
                    last_page = 1
                    for answer in current_answers:
                        if current_answers[answer]:
                            if answer[0] == 'p':
                                if answer[2] == 'q':
                                    page_num = answer[1:2]
                                    array_name = answer[:2]
                                    question_number = answer[3:]
                                elif answer[3]  == 'q':
                                    page_num = answer[1:3]
                                    array_name = answer[:3]
                                    question_number = answer[4:]
                                else:
                                    page_num = 1
                                    array_name = ''
                                    question_number = ''
                                if int(page_num) > last_page:
                                    last_page = int(page_num)

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
                    return redirect('page', last_page)
                except:
                    return redirect('page', 1)
            else:
                request.session['survey_user_id'] = current_student.id
                return redirect('/report')
        else:
            err_msg = "School - User - Continuation Password does not match database records. Please try again"
            request.session['continue_err_msg'] = err_msg

    return redirect('/#continue')


def save_survey(request):
    page_num = request.POST.get('pagenum','')
    if page_num != '':
        array_name = 'p' + str(page_num)
    else:
        request.session[save_error] = "incorrect page"
        return redirect('/')
    answer_array = request.POST.getlist(array_name + "[]")
    request.session[array_name] = answer_array
    row = {}
    answer_array = []
    for pagenum in range(1,12):
        page = "p" + str(pagenum)
        try:
            answer_array = request.session[page]
            answernum = 1
            for answer in answer_array:
                column = page + "q" + str(answernum)
                row[column] = answer
                answernum = answernum + 1
        except:
            pass

    current_student = Student.objects.filter(id=request.session['survey_user_id']).get()
    instance, created = AnswerSet.objects.get_or_create(student_id=current_student)
    for attr, value in row.iteritems():
        setattr(instance, attr, value)
    instance.save()

    request.session.flush()
    return redirect('/#continue')