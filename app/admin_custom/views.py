import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.validators import EmailValidator
from django.core.mail import send_mail
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils import timezone as tz
from .forms import (AdminLoginForm, SelectSurveyYearForm, SuperadminSelectSchoolForm,
  SuperadminCreateSchoolForm, AddStudentsBulkForm)
from survey.models import Student, School


User = get_user_model()


def public_login(request):
  context = {}
  context['admin_login_form'] = AdminLoginForm()
  if request.POST:
    form = AdminLoginForm(request.POST)
    if form.is_valid():
      user = authenticate(
        username=request.POST.get('email'), password=request.POST.get('password'))
      if user:
        login(request, user)
        if user.is_superuser:
          return redirect('superadmin_select_school')
        else:
          return redirect('admin_school_overview', user.school.id, tz.now().year)
    else:
      messages.error(request, 'Email address or password was not valid.')
      context['admin_login_form'] = form
  return render(request, "admin_custom/public_login.html", context)


def admin_school_overview(request, school_id, survey_year=None):
  context = {}
  context['admin_email'] = request.user.email
  context['school_id'] = school_id
  context['add_students_bulk_form'] = AddStudentsBulkForm()

  if not request.user.is_superuser:
    if int(school_id) != request.user.school.id:
      return redirect('admin_school_overview', request.user.school.id, tz.now().year)

  school = None
  try:
    school = School.objects.filter(id=school_id).get()
    context['admin_main_title'] = school.name
  except:
    print "WRONG SCHOOL ID"
    messages.error(request, "Could not process your request.")
    if request.user.is_superuser:
      return redirect('superadmin_select_school')
    else:
      return redirect('admin_school_overview', school_id=request.user.school.id, survey_year=survey_year)

  if survey_year:
    survey_year = int(survey_year)
    if survey_year <= 2014 or survey_year > 2030:
      messages.error(request, "Year out of range.")
      return redirect('admin_school_overview', school_id, tz.now().year)

    if survey_year not in school.get_survey_years():
      year = 0
      if len(school.get_survey_years()) > 0:
        year = max(school.get_survey_years())
      else:
        return redirect('admin_school_overview', school_id=school.id)
      messages.error(request, "There are no surveys for the year "+str(survey_year)+".")
      return redirect('admin_school_overview', school_id=school.id, survey_year=year)

  if len(school.get_survey_years()) > 0:
    print "HAS SURVEYS"
    context['select_survey_year_form'] = SelectSurveyYearForm(
        initial_year=survey_year, available_years=school.get_survey_years())
  else:
    print "NO SURVEYS"
    context['no_surveys_error'] = "No surveys exist for this school."

  return render(request, "admin_custom/school_overview.html", context)


def superadmin_overview(request):
  context = {}
  context['superadmin_select_school_form'] = SuperadminSelectSchoolForm()
  context['superadmin_create_school_form'] = SuperadminCreateSchoolForm()
  return render(request, "admin_custom/superadmin_overview.html", context)


def admin_select_survey_year(request, school_id):
  if request.POST:
    return redirect('admin_school_overview', int(school_id), int(request.POST.get('survey_year')))
  return redirect('admin_school_overview', int(school_id))



def admin_add_students_bulk(request):
  return


def admin_add_student_single(request):
  return