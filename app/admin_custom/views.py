import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils import timezone as tz
from .forms import (AdminLoginForm, SelectSurveyYearForm, SuperadminSelectSchoolForm,
  SuperadminCreateSchoolForm, AddStudentsBulkForm, AddSingleStudentForm,
  SuperadminCreateAdminForm)
from survey.models import Student, School


User = get_user_model()


def public_login(request):
  context = {}
  context['admin_login_form'] = AdminLoginForm()
  if request.method == 'POST':
    form = AdminLoginForm(request.POST)
    if form.is_valid():
      email = request.POST.get('email')
      pwd = request.POST.get('password')
      user = authenticate(username=email, password=pwd)
      if user:
        login(request, user)
        if user.is_superuser:
          request.session['school_id'] = None
          return redirect('superadmin_overview')
        else:
          request.session['school_id'] = user.school.id
          return redirect('admin_school_overview', school_id=user.school.id, survey_year=tz.now().year)
    else:
      messages.error(request, 'Email address or password was not valid.')
      context['admin_login_form'] = form
  return render(request, "admin_custom/public_login.html", context)


def admin_school_overview(request, school_id, survey_year=None):
  context = {}
  context['admin_email'] = request.user.email
  context['school_id'] = int(school_id)
  context['add_students_bulk_form'] = AddStudentsBulkForm()
  context['add_student_single_form'] = AddSingleStudentForm()

  school_id = int(school_id)

  students_list = []
  for student in enumerate(Student.objects.filter(school__id=school_id).values()):
    student[1]['index'] = student[0] + 1
    completed = False
    s = Student.objects.get(id=student[1]['id'], school__id=school_id)
    student[1]['completed'] = s.has_completed_survey_for_year(survey_year)

    students_list.append(student[1])
  if len(students_list) > 0:
    context['students_list'] = students_list

  request.session['school_id'] = school_id
  school = None
  try:
    school = School.objects.filter(id=school_id).get()
    context['admin_main_title'] = school.name
  except:
    messages.error(request, "Could not process your request.")
    if request.user.is_superuser:
      return redirect('superadmin_overview')
    else:
      return redirect('admin_school_overview', school_id=request.user.school.id, survey_year=survey_year)

  if not request.user.is_superuser:
    if int(school_id) != request.user.school.id:
      print request.user, "cannot access school:", school
      if school.has_surveys():
        year = max(school.get_survey_years())
        return redirect('admin_school_overview', school_id=school.id, survey_year=year)
      else:
        # if no surveys exist for a school for ANY year, then redirect to
        # admin_school_overview without the year url param
        return redirect('admin_school_overview', school_id=school.id, survey_year=None)

  # if year param in url
  if survey_year:
    survey_year = int(survey_year)
    request.session['survey_year'] = survey_year
    context['survey_year'] = survey_year
    year = None
    if survey_year <= 2014 or survey_year > 2030:
      messages.error(request, "Year out of range.")
      if school.has_surveys():
        year = max(school.get_survey_years())
        return redirect('admin_school_overview', school_id=school.id, survey_year=year)
      else:
        # if no surveys exist for a school for ANY year, then redirect to
        # admin_school_overview without the year url param
        return redirect('admin_school_overview', school_id=school.id)
    elif survey_year not in school.get_survey_years():
      if school.has_surveys():
        year = max(school.get_survey_years())
        messages.error(request, "There are no surveys for the year " +
          str(survey_year)+". The most current year in which students at " +
          school.name+" have taken the survey is "+str(year)+".")
        return redirect('admin_school_overview', school_id=school.id, survey_year=year)
      else:
        # if no surveys exist for a school for ANY year, then redirect to
        # admin_school_overview without the year url param
        return redirect('admin_school_overview', school_id=school.id)
  else:
    if school.has_surveys():
      year = max(school.get_survey_years())
      return redirect('admin_school_overview', school_id=school.id, survey_year=year)
    messages.info(request, "No students have taken the survey for this school for any year in which the survey has been distributed. There will be no data to access until a student submits a survey for this school. You may upload a list of students that are registered with "+school.name+". After this is completed, you can send out an email to all students notifying them of the survey.")
    return render(request, "admin_custom/school_overview.html", context)

  context['select_survey_year_form'] = SelectSurveyYearForm(
      initial_year=survey_year, available_years=school.get_survey_years())
  return render(request, "admin_custom/school_overview.html", context)


def superadmin_overview(request):
  context = {}
  context['superadmin_select_school_form'] = SuperadminSelectSchoolForm()
  context['superadmin_create_school_form'] = SuperadminCreateSchoolForm()
  context['superadmin_add_admin_form'] = SuperadminCreateAdminForm()
  context['schools_list'] = School.objects.all()
  context['admins_list'] = User.objects.all()
  if request.method == 'POST':
    select_school_form = SuperadminSelectSchoolForm(request.POST)
    if select_school_form.is_valid():
      school = School.objects.filter(id=request.POST.get('school')).get()
      if school.has_surveys():
        year = max(school.get_survey_years())
        return redirect('admin_school_overview', school_id=school.id, survey_year=year)
      else:
        # if no surveys exist for a school for ANY year, then redirect to
        # admin_school_overview without the year url param
        return redirect('admin_school_overview', school_id=school.id)
  return render(request, "admin_custom/superadmin_overview.html", context)


@require_http_methods(["POST"])
def superadmin_create_school(request):
  form = SuperadminCreateSchoolForm(request.POST)
  if form.is_valid():
    form.save()
  else:
    messages.error(request, "An error has occurred. Please try submitting the form again.")
  return redirect('superadmin_overview')


def admin_select_survey_year(request, school_id):
  school_id = int(school_id)
  if request.method == 'POST':
    return redirect('admin_school_overview', school_id=int(school_id), survey_year=int(request.POST.get('survey_year')))
  return redirect('admin_school_overview', school_id=int(school_id))


@require_http_methods(["POST"])
def admin_add_students_bulk(request, school_id):
  school_id = int(school_id)
  if not request.user.is_superuser:
    if int(school_id) != request.session.get('school_id'):
      print "wrong session"
      if request.session.get('survey_year'):
        return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
      return redirect('admin_school_overview', school_id=school_id)

  roster_form = AddStudentsBulkForm(request.POST, request.FILES)
  if (len(request.FILES.keys()) is 0) or (not roster_form.is_valid()):
    print "not valid"
    messages.error(request, "Please select a .csv file to upload.")
    if request.session.get('survey_year'):
      return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
    return redirect('admin_school_overview', school_id=school_id)

  if roster_form.is_valid():
    roster = []
    print "about to write chunks"
    for chunk in request.FILES['roster_file'].chunks():
      for line in chunk.strip().split('\n'):
        if len(line.split(',')) == 1:
          messages.error(request, "The file is not in the correct format.")
          if request.session.get('survey_year'):
            return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
          return redirect('admin_school_overview', school_id=school_id)
        uid = line.split(',')[0].strip()
        email = line.split(',')[1].strip()
        if uid == '' or email == '':
          messages.error(request, "The file is not in the correct format.")
          if request.session.get('survey_year'):
            return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
          return redirect('admin_school_overview', school_id=school_id)
        roster.append([uid, email])

    for student in roster:
      print "::", student

    if request.session.get('survey_year'):
      return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
    return redirect('admin_school_overview', school_id=school_id)

  messages.error(request, "An error has occurred. Please try uploading again.")
  if request.session.get('survey_year'):
    return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
  return redirect('admin_school_overview', school_id=school_id)


@require_http_methods(["POST"])
def admin_add_student_single(request, school_id):
  school_id = int(school_id)
  if not request.user.is_superuser:
    if int(school_id) != request.session.get('school_id'):
      print "wrong session"
      if request.session.get('survey_year'):
        return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
      return redirect('admin_school_overview', school_id=school_id)

  add_student_single_form = AddSingleStudentForm(request.POST)
  if add_student_single_form.is_valid():
    uid = request.POST.get('uid')
    email = request.POST.get('email')
    school = School.objects.get(id=school_id)
    student = Student.objects.create_student(uid, email, school)
    messages.success(request, 'Successfully added '+uid+' to '+school.name+'.')
  if request.session.get('survey_year'):
    return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
  return redirect('admin_school_overview', school_id=school_id)


def admin_delete_student(request, school_id, student_id):
  school_id = int(school_id)
  if not request.user.is_superuser:
    if int(school_id) != request.session.get('school_id'):
      print "wrong session"
      if request.session.get('survey_year'):
        return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
      return redirect('admin_school_overview', school_id=school_id)
  student = Student.objects.get(id=student_id, school__id=school_id)
  student.delete()
  messages.success(request, "Successfully deleted "+student.uid+".")
  if request.session.get('survey_year'):
    return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
  return redirect('admin_school_overview', school_id=school_id)


@require_http_methods(["POST"])
def admin_edit_student(request, school_id, student_id):
  school_id = int(school_id)
  if not request.user.is_superuser:
    if int(school_id) != request.session.get('school_id'):
      print "wrong session"
      if request.session.get('survey_year'):
        return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
      return redirect('admin_school_overview', school_id=school_id)

