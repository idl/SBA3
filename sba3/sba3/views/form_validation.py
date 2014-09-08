from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.loading import get_model

from ..forms import surveyLoginForm
from admin_custom.forms import LoginForm
from ..models import Student

def start_survey(request):
    if request.POST:
        school_id = request.POST.get('school', '')
        user_id = request.POST.get('identifier', '')
        survey_form = surveyLoginForm(request.POST)
        if user_id and survey_form.is_valid():
            try:
                new_student = Student.objects.create_student(user_id, school_id)
                request.session['user_id'] = new_student.user_id
                request.session['continue_pass'] = new_student.continue_pass
                return redirect('page', 1)
            except ValueError, e:
                request.session['err_msg'] = e
                redirect('/#survey')
        else:
            if school_id == '' and user_id == '':
                err_msg = 'School and Identifier fields cannot be blank.'
            elif school_id == '':
                err_msg = 'School field cannot be blank.'
            elif user_id == '':
                err_msg = 'Identifier field cannot be blank.'
            request.session['err_msg'] = err_msg
    return redirect('/#survey')