import datetime
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.validators import EmailValidator
from django.core.mail import send_mail
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .forms import AdminLoginForm
# from .models import User


def public_login(request):
  context = {
    'admin_login_form': AdminLoginForm(),
  }
  return render(request, "admin_custom/public_login.html", context)



# @login_required(redirect_field_name='')
# def admin(request, school_id=None, student_id=None):
#   ctx = {}
#   register_admin_err_msg = request.session.get('register_admin_err_msg', '')
#   request.session['register_admin_err_msg'] = []

#   success = request.session.get('success', '')
#   request.session['success'] = ''

#   update_admin_err_msg_list = request.session.get('update_admin_err_msg_list', '')
#   request.session['update_admin_err_msg_list'] = []

#   update_admin_err_id = request.session.get('update_admin_err_id', None)
#   request.session['update_admin_err_id'] = None

#   update_admin_success_msg = request.session.get('update_admin_success_msg', '')
#   request.session['update_admin_success_msg'] = ''

#   registerError = request.session.get('registerError', False)
#   request.session['registerError'] = False

#   registerSuccess = request.session.get('registerSuccess', False)
#   request.session['registerSuccess'] = False

#   survey_school_select = request.session.get('survey_school_select', '')
#   request.session['survey_school_select'] = ''

#   manage_err = request.session.get('manage_err', '')
#   request.session['manage_err'] = ''

#   school_list = School.objects.all()

#   survey_school_list = []
#   if request.POST:
#     survey_school_select = request.POST.get('survey_school_select', '')
#     dbprint("SSL: " + survey_school_select)
#     if survey_school_select != '':
#       return redirect('manage_roster', survey_school_select)
#     else:
#       return redirect('/admin/surveys')

#   superadmin_list = Users.objects.filter(is_superuser=True)
#   schooladmin_list = []
#   for user in Users.objects.filter(is_superuser=False).order_by('school_id'):
#     school_name = ''
#     try:
#       school_name = School.objects.get(id=user.school_id)
#     except:
#       continue
#     schooladmin_entry = {}
#     schooladmin_entry['id'] = user.id
#     schooladmin_entry['email'] = user.email
#     schooladmin_entry['school_id'] = user.school_id
#     schooladmin_entry['school_name'] = school_name
#     schooladmin_entry['last_login'] = user.last_login
#     schooladmin_entry['date_joined'] = user.date_joined
#     schooladmin_list.append(schooladmin_entry)

#   update_admin_err_msg = False
#   if len(update_admin_err_msg_list) > 0:
#     update_admin_err_msg = True

#   isSuperuser = request.user.is_superuser
#   currentUserEmail = Users.objects.get(id=request.user.id).email
#   currentSchoolId = Users.objects.get(id=request.user.id).school_id

#   ctx = { 'editGlobalAdminForm': EditGlobalAdminForm(auto_id='id_edit_globaladmin_%s'),
#       'editSchoolAdminForm': EditSchoolAdminForm(auto_id='id_edit_schooladmin_%s'),
#       'registerAdminForm': RegisterAdminForm(auto_id='id_register_admin_%s'),
#       'registerSchoolForm': RegisterSchoolForm(auto_id='id_register_school_%s'),
#       'register_admin_err_msg': register_admin_err_msg,
#       'update_admin_err_msg_list': update_admin_err_msg_list,
#       'update_admin_err_msg': update_admin_err_msg,
#       'update_admin_success_msg': update_admin_success_msg,
#       'success': success,
#       'registerError': registerError,
#       'registerSuccess': registerSuccess,
#       'school_list': school_list,
#       'superadmin_list': superadmin_list,
#       'schooladmin_list': schooladmin_list,
#       'manage_err': manage_err,
#       'isSuperuser': isSuperuser,
#       'currentUserEmail': currentUserEmail,
#       'currentSchoolId': currentSchoolId
#       }

#   if update_admin_err_id:
#     ctx['update_admin_err_id'] = update_admin_err_id
#   return render(request, 'admin_custom/admin.html', ctx)

# @login_required(redirect_field_name='')
# def create_school(request):
#   if request.POST:
#     school_name = request.POST.get('school_name', '')
#     school_location = request.POST.get('school_location', '')
#     survey_title = request.POST.get('survey_title', '')
#   if school_name == '':
#     request.session['registerError'] = True
#     request.session['registerSuccess'] = False
#   else:
#     try:
#       test = School.objects.filter(name=school_name).get()
#       request.session['registerError'] = True
#       request.session['registerSuccess'] = False
#     except:
#       new_school = School(
#         name=school_name,
#         location=school_location,
#         survey_title=survey_title,
#         date=datetime.date.today())
#       new_school.save()
#       request.session['registerError'] = False
#       request.session['registerSuccess'] = True
#       # vals = {
#       #   'name': request.POST['school_name'],
#       # }
#       # newSchool = School(**vals)
#       # newSchool.save()
#   return redirect('/admin/schools')

# @login_required
# def update_school(request, school_id):
#   if not school_permission_check(request.session['_auth_user_id'], school_id):
#     request.session['manage_err'] = "Not Authorized to edit this school"
#     return redirect('/admin/schools')

#   if not request.POST:
#     request.session['manage_err'] = 'Update school form error'
#     return redirect('/admin/schools')

#   name = request.POST.get('school_name', '')
#   location = request.POST.get('school_location', '')
#   survey_title = request.POST.get('survey_title', '')

#   if name == '':
#     request.session['manage_err'] = "Update School error - School must have a name"
#     return redirect('/admin/schools')

#   try:
#     School.objects.filter(id=school_id).update(name=name, location=location, survey_title=survey_title)
#   except:
#     request.session['manage_err'] = "Unknown Error while updating"

#   return redirect('/admin/schools')

# @login_required
# def delete_school(request, school_id):
#   if not school_permission_check(request.session['_auth_user_id'], school_id):
#     request.session['manage_err'] = "Not Authorized to edit this school"
#     return redirect('/admin/schools')

#   try:
#     student_list = Student.objects.filter(school_id=school_id)
#     if student_list:
#       for student in student_list:
#         try:
#           answers = AnswerSet.objects.filter(student_id=student).get()
#           answers.delete()
#         except:
#           pass

#       student_list.delete()
#   except:
#     pass

#   try:
#     SchoolUid.objects.filter(school_id=school_id).delete()
#   except:
#     pass

#   School.objects.filter(id=school_id).delete()
#   return redirect('/admin/schools')

# @login_required(redirect_field_name='')
# def register_admin(request):
#   # send_mail('Subject here', 'Here is the message.', 'sba3.test@gmail.com', ['sba3.test@gmail.com'], fail_silently=False)

#   if request.POST:
#     email = request.POST.get('email', '')
#     tmp_password = request.POST.get('tmp_password', '')
#     # password_confirm = request.POST.get('password_confirm', '')
#     school_id = request.POST.get('school', '')
#     is_superuser = request.POST.get('superuser', False)
#     register_admin_err_msg = []

#     if email == '' and tmp_password == '':
#       register_admin_err_msg.append('Email and temporary password fields cannot be blank.')
#     elif email == '':
#       register_admin_err_msg.append('Email cannot be blank.')
#     elif tmp_password == '':
#       register_admin_err_msg.append('Temporary password cannot be blank.')
#     # elif password_confirm == '':
#     #   register_admin_err_msg.append('Please confirm password.')

#     if (school_id == '' and is_superuser == False) or (school_id != '' and is_superuser == True):
#       register_admin_err_msg.append('New user <b>must</b> be either a School Admin '+
#                     'or a Global admin. Please verify that you '+
#                     'selected a school from the dropdown, or clicked '+
#                     'the checkbox indicating the Admin type is Global.')

#     # Custom form validation is already implemented above; reg_form.is_valid() is not needed
#     #
#     # reg_form = RegisterGlobalAdminForm(request.POST)
#     # if not reg_form.is_valid():
#       # register_admin_err_msg = ['Error processing form. Please ensure all fields are populated and the email address is in the correct format.']
#     try:
#       # if email is already registered
#       Users.objects.get(email=email)
#       register_admin_err_msg.append('Email address in use.')
#     except:
#       pass

#     if len(register_admin_err_msg) > 0:
#       request.session['register_admin_err_msg'] = register_admin_err_msg
#       return redirect('/admin/users')
#     if is_superuser == False:
#       Users.objects.create_user(email, tmp_password, school_id)
#       request.session['success'] = 'School admin created successfully!'
#     else:
#       Users.objects.create_superuser(email, tmp_password)
#       request.session['success'] = 'Superadmin created successfully!'
#   return redirect('/admin/users')

# @login_required
# def update_admin(request, admin_id):
#   if request.POST:
#     try:
#       usr = Users.objects.get(id=admin_id)
#     except:
#       request.session['update_admin_err_msg_list'] = ["Error updating user. Please try again."]
#       return redirect('/admin/users')
#     update_admin_err_msg_list = []
#     email = request.POST.get('email', None)
#     change_password = request.POST.get('change_password', None)
#     password = request.POST.get('password', None)
#     confirm_password = request.POST.get('confirm_password', None)
#     school = request.POST.get('school', None)
#     if(email == ''):
#       update_admin_err_msg_list.append('New email cannot be blank.')
#     if(change_password):
#       if(password == ''):
#         update_admin_err_msg_list.append('New password cannot be blank.')
#       if(confirm_password == ''):
#         update_admin_err_msg_list.append('Please confirm the password.')
#       if(password != confirm_password):
#         update_admin_err_msg_list.append('New password and its confirmation must match.')
#     if school == '':
#       update_admin_err_msg_list.append('Please pick a school.')
#     if len(update_admin_err_msg_list) > 0:
#       request.session['update_admin_err_msg_list'] = update_admin_err_msg_list
#       request.session['update_admin_err_id'] = admin_id
#       dbprint("ERRORS")
#       return redirect('/admin/users')
#     usr.email = email
#     usr.school_id = school
#     if change_password:
#       usr.set_password(password)
#     usr.save()
#     request.session['update_admin_success_msg'] = "User updated successfully."
#     return redirect('/admin/users')

# @login_required
# def delete_admin(request, admin_id):
#   usr = Users.objects.get(id=admin_id)
#   usr.delete()
#   return redirect('/admin/users')



# def login_view(request):
#   if request.user.is_authenticated():
#     return redirect('admin')
#   if request.POST:
#     email = request.POST.get('email', '').strip()
#     password = request.POST.get('password', '').strip()
#     user = authenticate(username=email, password=password)
#     login_form = LoginForm(request.POST)
#     if user and login_form.is_valid():
#       login(request, user)
#       return redirect('admin')
#     else:
#       login_err_msg = "Email and password combination doesn't match database records. Please try logging in again."
#       if email == '' and password == '':
#         login_err_msg = 'Email and password fields cannot be blank.'
#       elif email == '':
#         login_err_msg = 'Email cannot be blank.'
#       elif password == '':
#         login_err_msg = 'Password cannot be blank.'
#       # return render(request, 'home.html', { 'login_form': login_form, 'login_err_msg': login_err_msg })
#       request.session['login_err_msg'] = login_err_msg
#   return redirect('/admin')

# def logout_view(request):
#   logout(request)
#   return redirect('/#admin')

# def dbprint(input_str):
#   input_str = str(input_str)
#   output_str = '\n\n'
#   output_str += '#' * (len(input_str) + 4)
#   output_str += '\n'
#   output_str += '  ' + input_str.strip()
#   output_str += '\n'
#   output_str += '#' * (len(input_str) + 4)
#   output_str += '\n\n'
#   print output_str

# @login_required
# def manage_roster(request, school_id):
#   isSuperuser = request.user.is_superuser
#   if not school_permission_check(request.session['_auth_user_id'], school_id):
#     request.session['manage_err'] = "Not Authorized to edit this school roster"
#     return redirect('/admin/schools')

#   roster_uid_err = request.session.get('roster_uid_err', '')
#   request.session['roster_uid_err'] = ''

#   roster_file_err = request.session.get('roster_file_err', '')
#   request.session['roster_file_err'] = ''

#   uid_list = SchoolUid.objects.values_list('uid', flat=True).filter(school_id=school_id)
#   student_list = Student.objects.values().filter(school_id=school_id)
#   school = School.objects.get(id=school_id)
#   roster_list = {}
#   # dbprint(uid_list)
#   # dbprint(student_list)
#   if uid_list:
#     for uid in uid_list:
#       try:
#         student_info = student_list.filter(user_id__iexact=uid).get()
#         dbprint(student_info['id'])
#         roster_list[uid] = {
#           'active': 'Yes',
#           'continue': student_info['continue_pass'],
#           'complete': student_info['completed'],
#           'id': student_info['id']
#         }
#       except:
#         roster_list[uid] = {
#           'active': 'No',
#           'continue': 'Has not begun survey.',
#           'complete': 'No'
#         }
#   else:
#     if student_list:
#       for student in student_list:
#         roster_list[student['user_id']] = {
#           'active': 'Yes',
#           'continue': student['continue_pass'],
#           'complete': student['completed'],
#           'id': student['id']
#         }

#   ctx = {
#     'roster_list': roster_list,
#     'school': school,
#     'roster_uid_err': roster_uid_err,
#     'roster_file_err': roster_file_err,
#     'isSuperuser': isSuperuser,
#     'currentUserEmail': Users.objects.get(id=request.user.id).email
#   }
#   return render(request, 'roster.html', ctx)


# @login_required
# def update_roster(request, school_id):
#   if not school_permission_check(request.session['_auth_user_id'], school_id):
#     request.session['manage_err'] = "Not Authorized to edit this school roster"
#     return redirect('/admin/schools')

#   uid = request.POST.get('uid', '')

#   if uid == '':
#     request.session['roster_uid_err'] = 'No user id provided'
#     return redirect('/admin/'+str(school_id)+'/roster')

#   school = School.objects.filter(id=school_id).get()

#   try:
#     test = SchoolUid.objects.filter(uid=uid, school_id=school_id).get()
#     request.session['roster_uid_err'] = 'User id already exists'
#     return redirect('/admin/'+str(school_id)+'/roster')
#   except:
#     pass

#   uid_instance = SchoolUid(school_id=school, uid=uid)
#   uid_instance.save()

#   return redirect('/admin/'+str(school_id)+'/roster')

# @login_required
# def remove_roster(request, school_id, uid):
#   if not school_permission_check(request.session['_auth_user_id'], school_id):
#     request.session['manage_err'] = "Not Authorized to edit this school roster"
#     return redirect('/admin/schools')

#   if uid == '':
#     request.session['roster_uid_err'] = 'No user id provided'
#     return redirect('/admin/'+str(school_id)+'/roster')

#   try:
#     student = Student.objects.filter(user_id=uid, school_id=school_id).get()

#     try:
#       answers = AnswerSet.objects.filter(student_id=student).get()
#       answers.delete()
#     except:
#       pass

#     student.delete()
#   except:
#     pass

#   SchoolUid.objects.filter(uid=uid, school_id=school_id).delete()
#   return redirect('/admin/'+str(school_id)+'/roster')

# @login_required
# def upload_roster(request, school_id):
#   if not school_permission_check(request.session['_auth_user_id'], school_id):
#     request.session['manage_err'] = "Not Authorized to edit this school roster"
#     return redirect('/admin/schools')

#   roster_file = request.FILES.get('uid_list', False)
#   if not roster_file:
#     request.session['roster_file_err'] = "File Error"
#     return redirect('/admin/'+str(school_id)+'/roster')

#   new_uid_list = []
#   uid_list = SchoolUid.objects.values_list('uid', flat=True).filter(school_id=school_id)

#   school = School.objects.filter(id=school_id).get()

#   try:
#     for line in roster_file:
#       line = line.rstrip('\n')
#       values = line.split(",")
#       for uid in values:
#         if uid[:1] == ' ':
#           uid = uid[1:]

#         if uid in uid_list:
#           continue
#         else:
#           new_uid_list.append(
#             SchoolUid(
#               school_id=school,
#               uid=uid
#             )
#           )
#     SchoolUid.objects.bulk_create(new_uid_list)
#   except:
#     request.session['roster_file_err'] = "File Error"

#   return redirect('/admin/'+str(school_id)+'/roster')


# def school_permission_check(user_id, school_id):
#   try:
#     user_info = User.objects.values('is_superuser', 'school_id').filter(id=user_id).get()
#   except:
#     return False

#   if user_info['is_superuser']:
#     return True

#   if user_info['school_id'] == school_id:
#     return True

#   return False



# def survey_data_school_individual(request, school_id, student_id):
#   ctx = {}
#   ctx['school_id'] = school_id
#   try: 
#     ctx['user_id'] = Student.objects.get(id=student_id).user_id
#     ctx['results'] = AnswerSet.objects.values().get(student_id_id=student_id)
#     return render(request, "school_student_data.html", ctx)
#   except:
#     return render(request, "school_student_data_error.html", ctx)

# def survey_data_school_aggregate(request, school_id):
#   ctx = {}
#   return render(request, "school_data_viewall.html", ctx)

















