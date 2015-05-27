import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.core.validators import validate_email
from django.utils import timezone as tz
from .forms import (AdminLoginForm, SelectSurveyYearForm, SuperadminSelectSchoolForm,
  SuperadminCreateEditSchoolForm, CreateStudentsBulkForm, CreateEditStudentForm,
  SuperadminCreateEditAdminForm, AdminEditAccountEmailForm, AdminEditAccountPasswordForm)
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


@login_required(redirect_field_name=None)
def public_logout(request):
  logout(request)
  return redirect('public_admin_login')


#******************************#
#****** SuperAdmin Views ******#
#******************************#

@login_required(redirect_field_name=None)
@user_passes_test(lambda u: u.is_superuser)
@require_http_methods(['POST'])
def superadmin_create_admin(request):
  form = SuperadminCreateEditAdminForm(request.POST)
  # is school admin - school select didn't return None causing is_valid() to
  # be be True -- therefore create school admin
  email = request.POST.get('email')
  password = request.POST.get('password')
  is_superuser = request.POST.get('is_superuser')
  school = None
  try:
    print request.POST.get('school')
    school = School.objects.get(id=request.POST.get('school'))
    print school
  except:
    if not is_superuser:
      messages.error(request, 'An error has occured. Please try creating the user again.')
      return redirect('superadmin_overview')

  if User.objects.filter(email=email).count() > 0:
    messages.error(request, 'That email address is already in use. Please use a different email.')
    return redirect('superadmin_overview')

  if is_superuser:
    User.objects.create_superuser(email, password)
  else:
    User.objects.create_user(email, password, school)
  messages.success(request, 'Successfully created administrator '+email+'.')
  return redirect('superadmin_overview')

@login_required(redirect_field_name=None)
@user_passes_test(lambda u: u.is_superuser)
def superadmin_delete_admin(request, admin_id):
  if request.user.id == int(admin_id):
    messages.error(request, 'You cannot delete your own account.')
    return redirect('superadmin_overview')
  if not request.user.is_superuser:
    return redirect('superadmin_overview')
  try:
    user = User.objects.get(id=admin_id)
    user.delete()
  except:
    return redirect('superadmin_overview')
  messages.success(request, 'Successfully deleted administrator '+user.email+'.')
  return redirect('superadmin_overview')


@login_required(redirect_field_name=None)
@user_passes_test(lambda u: u.is_superuser)
@require_http_methods(['POST'])
def superadmin_edit_admin(request, admin_id):
  email = request.POST.get('email')
  change_password = request.POST.get('change_password')
  password = request.POST.get('password')
  confirm_password = request.POST.get('confirm_password')
  is_superuser = request.POST.get('is_superuser')
  school = request.POST.get('school')
  error = False

  def set_session_err(request):
    request.session['update_admin_error'] = True
    request.session['update_admin_error_email'] = email
    request.session['update_admin_error_admin_id'] = admin_id
    request.session['update_admin_error_is_superuser'] = is_superuser
    request.session['update_admin_error_school'] = school

  user = None
  try:
    user = User.objects.get(id=admin_id)
  except:
    return redirect('superadmin_overview')

  try:
    validate_email(email)
    user.email = email
  except:
    messages.error(request, 'Please enter a valid email when updating admin.')
    error = True

  if int(admin_id) == request.user.id:
    if is_superuser == None:
      set_session_err(request)
      request.session['update_admin_error_is_superuser'] = True
      messages.error(request, 'Cannot downgrade the status of your own account.')
      return redirect('superadmin_overview')

  if change_password:
    if password != confirm_password:
      messages.error(request, 'Please ensure passwords match when updating admin.')
      set_session_err(request)
      return redirect('superadmin_overview')

    if len(password) is 0 or len(confirm_password) is 0:
      messages.error(request, 'Please ensure you have entered a password in both fields.')
      set_session_err(request)
      return redirect('superadmin_overview')

    user.set_password(password)

  if error:
    set_session_err(request)
    return redirect('superadmin_overview')

  if is_superuser:
    user.school = None
    user.is_superuser = True
  else:
    user.is_superuser = False
    try:
      user.school = School.objects.get(id=int(school))
    except:
      messages.error(request, 'An unknown error occurred.')
      return redirect('superadmin_overview')
  user.save()
  messages.success(request, 'Successfully updated user '+user.email+'.')
  return redirect('superadmin_overview')


@login_required(redirect_field_name=None)
@user_passes_test(lambda u: u.is_superuser)
@require_http_methods(['POST'])
def superadmin_edit_school(request, school_id):
  name = request.POST.get('name')
  location = request.POST.get('location')
  survey_title = request.POST.get('survey_title')
  error = False
  school = None

  def set_session_err(request):
    request.session['update_school_error'] = True
    request.session['update_school_error_name'] = name
    request.session['update_school_error_location'] = location
    request.session['update_school_error_school_id'] = school_id
    request.session['update_school_error_survey_title'] = survey_title

  try:
    school = School.objects.get(id=school_id)
  except:
    messages.error(request, 'An unknown error occurred. Please try updating the school again.')
    return render('superadmin_overview')

  if name.strip() == '':
    messages.error(request, 'Please enter a school name.')
    error = True
  if location.strip() == '':
    messages.error(request, 'Please enter a location.')
    error = True
  if location.strip() == '':
    messages.error(request, 'Please enter a location.')
    error = True
  if error:
    set_session_err(request)
    return redirect('superadmin_overview')

  school.name = name
  school.location = location
  if survey_title != None:
    school.survey_title = survey_title
  school.save()
  messages.success(request, 'Successfully updated school '+school.name+'.')
  return redirect('superadmin_overview')


@login_required(redirect_field_name=None)
@user_passes_test(lambda u: u.is_superuser)
def superadmin_delete_school(request, school_id):
  if not request.user.is_superuser:
    return redirect('superadmin_overview')
  try:
    school = School.objects.get(id=school_id)
    school.delete()
  except:
    return redirect('superadmin_overview')
  messages.success(request, 'Successfully deleted school '+school.name+'.')
  return redirect('superadmin_overview')


@login_required(redirect_field_name=None)
@user_passes_test(lambda u: u.is_superuser)
@require_http_methods(["POST"])
def superadmin_create_school(request):
  form = SuperadminCreateEditSchoolForm(request.POST)
  if form.is_valid():
    form.save()
  else:
    messages.error(request, "An error has occurred. Please try submitting the form again.")
  return redirect('superadmin_overview')


@login_required(redirect_field_name=None)
@user_passes_test(lambda u: u.is_superuser)
def superadmin_overview(request):
  context = {}
  context['superadmin_select_school_form'] = SuperadminSelectSchoolForm()
  context['superadmin_create_admin_form'] = SuperadminCreateEditAdminForm()
  context['superadmin_create_school_form'] = SuperadminCreateEditSchoolForm()
  context['superadmin_edit_admin_form'] = SuperadminCreateEditAdminForm(is_modal=True)
  context['superadmin_edit_school_form'] = SuperadminCreateEditSchoolForm(is_modal=True)
  # .extra() does case-insensitive ordering by name
  context['schools_list'] = School.objects.all().order_by('name_lower').extra(select={'name_lower': 'lower(name)'})
  context['admins_list'] = User.objects.all().order_by('-is_superuser', 'school')
  context['admin_email'] = request.user.email

  if not request.user.is_superuser:
    return redirect('admin_school_overview', request.user.school.id)

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

  if request.session.get('update_admin_error'):
    context['update_admin_error'] = True
    context['update_admin_error_email'] = request.session['update_admin_error_email']
    context['update_admin_error_admin_id'] = request.session['update_admin_error_admin_id']
    context['update_admin_error_school'] = request.session['update_admin_error_school']
    context['update_admin_error_is_superuser'] = request.session['update_admin_error_is_superuser']
    del request.session['update_admin_error']
    del request.session['update_admin_error_email']
    del request.session['update_admin_error_admin_id']
    del request.session['update_admin_error_school']
    del request.session['update_admin_error_is_superuser']

  if request.session.get('update_school_error'):
    context['update_school_error'] = True
    context['update_school_error_name'] = request.session['update_school_error_name']
    context['update_school_error_location'] = request.session['update_school_error_location']
    context['update_school_error_school_id'] = request.session['update_school_error_school_id']
    context['update_school_error_survey_title'] = request.session['update_school_error_survey_title']
    del request.session['update_school_error']
    del request.session['update_school_error_name']
    del request.session['update_school_error_location']
    del request.session['update_school_error_school_id']
    del request.session['update_school_error_survey_title']

  return render(request, "admin_custom/superadmin_overview.html", context)





#********************************#
#****** School Admin Views ******#
#********************************#

@login_required(redirect_field_name=None)
def admin_school_overview(request, school_id, survey_year=None):
  context = {}
  context['admin_email'] = request.user.email
  context['school_id'] = int(school_id)
  context['create_students_bulk_form'] = CreateStudentsBulkForm()
  context['create_student_single_form'] = CreateEditStudentForm()
  context['admin_edit_student_form'] = CreateEditStudentForm(is_modal=True)

  school_id = int(school_id)
  students = Student.objects.filter(school__id=school_id)
  students_list = []
  for student in enumerate(students.order_by('uid').values()):
    student[1]['index'] = student[0] + 1
    completed = False
    s = Student.objects.get(id=student[1]['id'], school__id=school_id)
    student[1]['completed'] = s.has_completed_survey_for_year(survey_year)
    student[1]['started'] = s.has_started_survey_for_year(survey_year)
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
      return redirect('admin_school_overview', school_id=request.user.school.id)

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

  if request.session.get('update_student_error'):
    print "ERROR"
    context['update_student_error'] = True
    context['update_student_error_uid'] = request.session['update_student_error_uid']
    context['update_student_error_email'] = request.session['update_student_error_email']
    context['update_student_error_student_id'] = request.session['update_student_error_student_id']
    del request.session['update_student_error']
    del request.session['update_student_error_uid']
    del request.session['update_student_error_email']
    del request.session['update_student_error_student_id']

  context['select_survey_year_form'] = SelectSurveyYearForm(
      initial_year=survey_year, available_years=school.get_survey_years())
  return render(request, "admin_custom/school_overview.html", context)


@login_required(redirect_field_name=None)
def admin_select_survey_year(request, school_id):
  school_id = int(school_id)
  if request.method == 'POST':
    return redirect('admin_school_overview', school_id=int(school_id), survey_year=int(request.POST.get('survey_year')))
  return redirect('admin_school_overview', school_id=int(school_id))


@login_required(redirect_field_name=None)
@require_http_methods(["POST"])
def admin_create_students_bulk(request, school_id):
  school_id = int(school_id)
  if not request.user.is_superuser:
    if int(school_id) != request.session.get('school_id'):
      print "wrong session"
      if request.session.get('survey_year'):
        return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
      return redirect('admin_school_overview', school_id=school_id)

  roster_form = CreateStudentsBulkForm(request.POST, request.FILES)
  if (len(request.FILES.keys()) is 0) or (not roster_form.is_valid()):
    print "not valid"
    messages.error(request, "Please select a .csv file to upload.")
    if request.session.get('survey_year'):
      return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
    return redirect('admin_school_overview', school_id=school_id)

  if roster_form.is_valid():
    roster = []
    emails = []
    uids = []
    print "about to write chunks"
    for chunk in request.FILES['roster_file'].chunks():
      for line in chunk.strip().split('\n'):
        if len(line.split(',')) == 1:
          messages.error(request, "The file is not in the correct format. Please try reuploading the file.")
          if request.session.get('survey_year'):
            return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
          return redirect('admin_school_overview', school_id=school_id)
        uid = line.split(',')[0].strip()
        email = line.split(',')[1].strip()
        if uid == '' or email == '':
          messages.error(request, "The file is not in the correct format. Please try reuploading the file.")
          if request.session.get('survey_year'):
            return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
          return redirect('admin_school_overview', school_id=school_id)
        roster.append([uid, email])
        if Student.objects.filter(school__id=school_id, email=email).count() > 0:
          messages.error(request, "There is already a student that exists with the email "+email+". Please try reuploading an updated file.")
          return redirect('admin_school_overview', school_id=school_id)
        if Student.objects.filter(school__id=school_id, uid=uid).count() > 0:
          messages.error(request, "There is already a student that exists with the identifier "+uid+". Please try reuploading an updated file.")
          return redirect('admin_school_overview', school_id=school_id)
        if email in emails:
          messages.error(request, "Students cannot have duplicate email addresses. Please try reuploading the file.")
          return redirect('admin_school_overview', school_id=school_id)
        if uid in uids:
          messages.error(request, "Students cannot have duplicate identifiers (UID). Please try reuploading the file.")
          return redirect('admin_school_overview', school_id=school_id)
        emails.append(email)

    school = None
    try:
      school = School.objects.get(id=school_id)
    except:
      messages.error(request, "An error occurred. Please try reuploading the file again.")
      return redirect('admin_school_overview', school_id=school_id)

    for student in roster:
      Student.objects.create_student(student[0], student[1], school)

    if request.session.get('survey_year'):
      return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
    return redirect('admin_school_overview', school_id=school_id)

  messages.error(request, "An error has occurred. Please try uploading again.")
  if request.session.get('survey_year'):
    return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
  return redirect('admin_school_overview', school_id=school_id)


@login_required(redirect_field_name=None)
@require_http_methods(["POST"])
def admin_create_student_single(request, school_id):
  school_id = int(school_id)
  if not request.user.is_superuser:
    if int(school_id) != request.session.get('school_id'):
      print "wrong session"
      if request.session.get('survey_year'):
        return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
      return redirect('admin_school_overview', school_id=school_id)

  if Student.objects.filter(school__id=school_id, uid=request.POST.get('uid')).count() > 0:
    messages.error(request, "Students cannot have duplicate identifiers (UID). A student with the UID "+request.POST.get('uid')+" already exists.")
    return redirect('admin_school_overview', school_id=school_id)

  if Student.objects.filter(school__id=school_id, email=request.POST.get('email')).count() > 0:
    messages.error(request, "Students cannot have duplicate email addresses. A student with the email "+request.POST.get('email')+" already exists.")
    return redirect('admin_school_overview', school_id=school_id)

  uid = request.POST.get('uid')
  email = request.POST.get('email')
  school = None
  try:
    school = School.objects.get(id=school_id)
  except:
    messages.error(request, "An error occurred. Please try again.")
    return redirect('admin_school_overview', school_id=school_id)

  try:
    validate_email(email)
  except:
    messages.error(request, 'Please enter a valid email when creating student.')
    return redirect('admin_school_overview', school_id=school_id)
  if uid.strip() == '' or email.strip() == '':
    messages.error(request, 'Please fill out both fields and ensure email is in the correct format.')
    return redirect('admin_school_overview', school_id=school_id)

  student = Student.objects.create_student(uid, email, school)
  messages.success(request, 'Successfully added '+uid+' to '+school.name+'.')
  if request.session.get('survey_year'):
    return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
  return redirect('admin_school_overview', school_id=school_id)


@login_required(redirect_field_name=None)
def admin_delete_student(request, school_id, student_id):
  school_id = int(school_id)
  if not request.user.is_superuser:
    if int(school_id) != request.session.get('school_id'):
      print "wrong session"
      if request.session.get('survey_year'):
        return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
      return redirect('admin_school_overview', school_id=school_id)
  student = None
  try:
    student = Student.objects.get(id=student_id, school__id=school_id)
  except:
    messages.error(request, "An error occurred. Please try again.")
    return redirect('admin_school_overview', school_id=school_id)
  student.delete()
  messages.success(request, "Successfully deleted "+student.uid+".")
  if request.session.get('survey_year'):
    return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
  return redirect('admin_school_overview', school_id=school_id)


@login_required(redirect_field_name=None)
@require_http_methods(["POST"])
def admin_edit_student(request, school_id, student_id):
  school_id = int(school_id)
  if not request.user.is_superuser:
    if int(school_id) != request.session.get('school_id'):
      print "wrong session"
      if request.session.get('survey_year'):
        return redirect('admin_school_overview', school_id=school_id, survey_year=request.session.get('survey_year'))
      return redirect('admin_school_overview', school_id=school_id)

  uid = request.POST.get('uid')
  email = request.POST.get('email')

  def set_session_err(request):
    request.session['update_student_error'] = True
    request.session['update_student_error_uid'] = uid
    request.session['update_student_error_email'] = email
    request.session['update_student_error_student_id'] = student_id

  if uid.strip() == '' or email.strip() == '':
    set_session_err(request)
    messages.error(request, 'Please fill out both fields and ensure email is in the correct format.')
    return redirect('admin_school_overview', school_id=school_id)

  try:
    validate_email(email)
  except:
    set_session_err(request)
    messages.error(request, 'Please enter a valid email when updating student.')
    return redirect('admin_school_overview', school_id=school_id)

  student = None
  try:
    student = Student.objects.get(school__id=school_id, id=student_id)
  except:
    set_session_err(request)
    messages.error(request, 'Please enter a valid email when updating student.')
    return redirect('admin_school_overview', school_id=school_id)
  student.uid = uid
  student.email = email
  student.save()
  messages.success(request, "Successfully updated "+student.uid+".")
  return redirect('admin_school_overview', school_id=school_id)


@login_required(redirect_field_name=None)
def admin_edit_account(request):
  context = {}

  email_form = AdminEditAccountEmailForm(instance=request.user)
  context['edit_account_email_form'] = email_form
  context['edit_account_password_form'] = AdminEditAccountPasswordForm()

  if request.method == 'POST':
    email_form = AdminEditAccountEmailForm(request.POST, instance=request.user)
    password_form = AdminEditAccountPasswordForm(request.POST)
    context['edit_account_email_form'] = email_form
    if email_form.is_valid():
      request.user.email = request.POST.get('email')
      request.user.save()
      messages.success(request, "Successfully updated your email address.")
    else:
      messages.error(request, "Please ensure email is in the correct format.")

    if request.POST.get('change_password'):
      pwd = request.POST.get('password').strip()
      confpwd = request.POST.get('confirm_password').strip()
      error = False
      if pwd == '' or confpwd == '':
        error = True
        messages.error(request, "Please fill out both fields to change password.")
      if pwd != confpwd:
        error = True
        messages.error(request, "Passwords must match.")
      if error:
        context['update_password_error'] = True
        return render(request, 'admin_custom/edit_account.html', context)
      messages.success(request, "Successfully updated your password.")
      request.user.set_password(pwd)

  return render(request, 'admin_custom/edit_account.html', context)