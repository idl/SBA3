from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.validators import EmailValidator
from django.core.mail import send_mail
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .forms import *
from sba3.models import School

Users = get_user_model()

@login_required(redirect_field_name='')
def admin(request):
	register_admin_err_msg = request.session.get('register_admin_err_msg', '')
	success = request.session.get('success', '')
	update_admin_err_msg_list = request.session.get('update_admin_err_msg_list', '')
	update_admin_err_msg = False
	update_admin_err_id = request.session.get('update_admin_err_id', None)
	update_admin_success_msg = request.session.get('update_admin_success_msg', '')
	request.session['register_admin_err_msg'] = []
	request.session['login_err_msg'] = ''
	request.session['success'] = ''
	request.session['update_admin_err_msg_list'] = []
	request.session['update_admin_err_id'] = None
	request.session['update_admin_success_msg'] = ''
	registerError = request.session.get('registerError', False)
	registerSuccess = request.session.get('registerSuccess', False)
	request.session['registerError'] = False
	request.session['registerSuccess'] = False

	school_list = School.objects.all()
	superadmin_list = Users.objects.filter(is_superuser=True)
	schooladmin_list = []
	for user in Users.objects.filter(is_superuser=False).order_by('school_id'):
		schooladmin_entry = {}
		schooladmin_entry['id'] = user.id
		schooladmin_entry['email'] = user.email
		schooladmin_entry['school_id'] = user.school_id
		schooladmin_entry['school_name'] = School.objects.get(id=user.school_id)
		schooladmin_entry['last_login'] = user.last_login
		schooladmin_entry['date_joined'] = user.date_joined
		schooladmin_list.append(schooladmin_entry)
	if len(update_admin_err_msg_list) > 0:
		update_admin_err_msg = True

	ctx = { 'editGlobalAdminForm': EditGlobalAdminForm(auto_id='id_edit_globaladmin_%s'),
			'editSchoolAdminForm': EditSchoolAdminForm(auto_id='id_edit_schooladmin_%s'),
			'registerAdminForm': RegisterAdminForm(auto_id='id_register_admin_%s'),
			'registerSchoolForm': RegisterSchoolForm(auto_id='id_register_school_%s'),
			'register_admin_err_msg': register_admin_err_msg,
			'update_admin_err_msg_list': update_admin_err_msg_list,
			'update_admin_err_msg': update_admin_err_msg,
			'update_admin_success_msg': update_admin_success_msg,
			'success': success,
			'registerError': registerError,
			'registerSuccess': registerSuccess,
			'school_list': school_list,
			'superadmin_list': superadmin_list,
			'schooladmin_list': schooladmin_list
		  }
	if update_admin_err_id:
		ctx['update_admin_err_id'] = update_admin_err_id
	return render(request, 'admin_custom/admin.html', ctx)


@login_required(redirect_field_name='')
def create_school(request):
	if request.POST:
		school_name = request.POST.get('school_name', '')
	if school_name == '':
		request.session['registerError'] = True
		request.session['registerSuccess'] = False
	else:
		try:
			test = School.objects.filter(name=school_name).get()
			request.session['registerError'] = True
			request.session['registerSuccess'] = False
		except:
			new_school = School(name=school_name)
			new_school.save()
			request.session['registerError'] = False
			request.session['registerSuccess'] = True
			# vals = { 
			# 	'name': request.POST['school_name'],
			# }
			# newSchool = School(**vals)
			# newSchool.save()
	return redirect('/admin/#registerschools')

@login_required(redirect_field_name='')
def register_admin(request):
	# send_mail('Subject here', 'Here is the message.', 'sba3.test@gmail.com', ['sba3.test@gmail.com'], fail_silently=False)

	if request.POST:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
		email = request.POST.get('email', '')
		tmp_password = request.POST.get('tmp_password', '')
		# password_confirm = request.POST.get('password_confirm', '')
		school_id = request.POST.get('school', '')
		is_superuser = request.POST.get('superuser', False)
		register_admin_err_msg = []

		if email == '' and tmp_password == '':
			register_admin_err_msg.append('Email and temporary password fields cannot be blank.')
		elif email == '':
			register_admin_err_msg.append('Email cannot be blank.')
		elif tmp_password == '':
			register_admin_err_msg.append('Temporary password cannot be blank.')
		# elif password_confirm == '':
		# 	register_admin_err_msg.append('Please confirm password.')
		
		if (school_id == '' and is_superuser == False) or (school_id != '' and is_superuser == True):
			register_admin_err_msg.append('New user <b>must</b> be either a School Admin or a Global admin.')

		# Custom form validation is already implemented above; reg_form.is_valid() is not needed
		#
		# reg_form = RegisterGlobalAdminForm(request.POST)
		# if not reg_form.is_valid():
			# register_admin_err_msg = ['Error processing form. Please ensure all fields are populated and the email address is in the correct format.']
		try:
			# if email is already registered
			Users.objects.get(email=email)
			register_admin_err_msg.append('Email address in use.')
		except:
			pass

		if len(register_admin_err_msg) > 0:
			request.session['register_admin_err_msg'] = register_admin_err_msg
			return redirect('/admin/#users')
		if is_superuser == False:
			Users.objects.create_user(email, tmp_password, school_id)
			request.session['success'] = 'School admin created successfully!'
		else:
			Users.objects.create_superuser(email, tmp_password)
			request.session['success'] = 'Superadmin created successfully!'
	return redirect('/admin/#users')

@login_required
def update_admin(request, admin_id):
	if request.POST:
		try:	
			usr = Users.objects.get(id=admin_id)
		except:
			request.session['update_admin_err_msg_list'] = ["Error updating user. Please try again."]
			return redirect('/admin/#users')
		update_admin_err_msg_list = []
		email = request.POST.get('email', None)
		change_password = request.POST.get('change_password', None)
		password = request.POST.get('password', None)
		confirm_password = request.POST.get('confirm_password', None)
		school = request.POST.get('school', None)
		if(email == ''):
			update_admin_err_msg_list.append('New email cannot be blank.')
		if(change_password):
			if(password == ''):
				update_admin_err_msg_list.append('New password cannot be blank.')
			if(confirm_password == ''):
				update_admin_err_msg_list.append('Please confirm the password.')
			if(password != confirm_password):
				update_admin_err_msg_list.append('New password and its confirmation must match.')
		if school == '':
			update_admin_err_msg_list.append('Please pick a school.')
		if len(update_admin_err_msg_list) > 0:
			request.session['update_admin_err_msg_list'] = update_admin_err_msg_list
			request.session['update_admin_err_id'] = admin_id
			dbprint("ERRORS")
			return redirect('/admin/#users')
		usr.email = email
		usr.school_id = school
		if change_password:
			usr.set_password(password)
		usr.save()
		request.session['update_admin_success_msg'] = "User updated successfully."
		return redirect('/admin/#users')

def delete_admin(request, admin_id):
	usr = Users.objects.get(id=admin_id)
	usr.delete()
	return redirect('/admin/#users')

def login_view(request):
	if request.user.is_authenticated():
		return redirect('admin')
	if request.POST:
		email = request.POST.get('email', '').strip()
		password = request.POST.get('password', '').strip()
		user = authenticate(username=email, password=password)
		login_form = LoginForm(request.POST)
		if user and login_form.is_valid():
			if login(request, user):
				return redirect('login_view')
			else:
				login_err_msg = "Email and password combination doesn't match database records. Please try logging in again."
				request.session['login_err_msg'] = login_err_msg
		else:
			login_err_msg = "Email and password combination doesn't match database records. Please try logging in again."
			if email == '' and password == '':
				login_err_msg = 'Email and password fields cannot be blank.'
			elif email == '':
				login_err_msg = 'Email cannot be blank.'
			elif password == '':
				login_err_msg = 'Password cannot be blank.'
			# return render(request, 'home.html', { 'login_form': login_form, 'login_err_msg': login_err_msg })
			request.session['login_err_msg'] = login_err_msg
	return redirect('/#admin')

def logout_view(request):
	logout(request)
	return redirect('login_view')

def dbprint(input_str):
	input_str = str(input_str)
	output_str = '\n\n'
	output_str += '#' * (len(input_str) + 4)
	output_str += '\n'
	output_str += '  ' + input_str.strip()
	output_str += '\n'
	output_str += '#' * (len(input_str) + 4)
	output_str += '\n\n'
	print output_str
