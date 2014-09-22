from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.validators import EmailValidator
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .forms import LoginForm, RegisterAdminForm, RegisterSchoolForm, EditGlobalAdminForm
from sba3.models import School

Users = get_user_model()

@login_required(redirect_field_name='')
def admin(request):
	err_msg = request.session.get('err_msg', '')
	success = request.session.get('success', '')
	request.session['err_msg'] = ''
	request.session['login_err_msg'] = ''
	request.session['success'] = ''
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
		schooladmin_entry['school'] = School.objects.get(id=user.school_id)
		schooladmin_entry['last_login'] = user.last_login
		schooladmin_entry['date_joined'] = user.date_joined
		schooladmin_list.append(schooladmin_entry)
	ctx = { 'editGlobalAdminForm': EditGlobalAdminForm(),
			'registerAdminForm': RegisterAdminForm(),
			'registerSchoolForm': RegisterSchoolForm(),
			'err_msg': err_msg,
			'success': success,
			'registerError': registerError,
			'registerSuccess': registerSuccess,
			'school_list': school_list,
			'superadmin_list': superadmin_list,
			'schooladmin_list': schooladmin_list
		  }
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
	if request.POST:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
		email = request.POST.get('email', '')
		tmp_password = request.POST.get('tmp_password', '')
		# password_confirm = request.POST.get('password_confirm', '')
		school_id = request.POST.get('school', '')
		is_superuser = request.POST.get('superuser', False)
		err_msg = []

		if email == '' and tmp_password == '':
			err_msg.append('Email and temporary password fields cannot be blank.')
		elif email == '':
			err_msg.append('Email cannot be blank.')
		elif tmp_password == '':
			err_msg.append('Temporary password cannot be blank.')
		# elif password_confirm == '':
		# 	err_msg.append('Please confirm password.')
		
		if (school_id == '' and is_superuser == False) or (school_id != '' and is_superuser == True):
			err_msg.append('New user <b>must</b> be either a School Admin or a Global admin.')

		# Custom form validation is already implemented above; reg_form.is_valid() is not needed
		#
		# reg_form = RegisterGlobalAdminForm(request.POST)
		# if not reg_form.is_valid():
			# err_msg = ['Error processing form. Please ensure all fields are populated and the email address is in the correct format.']
		try:
			# if email is already registered
			Users.objects.get(email=email)
			err_msg.append('Email address in use.')
		except:
			pass

		if len(err_msg) > 0:
			request.session['err_msg'] = err_msg
			return redirect('/admin/#users')
		if is_superuser == False:
			Users.objects.create_user(email, tmp_password, school_id)
			request.session['success'] = 'School admin created successfully!'
		else:
			Users.objects.create_superuser(email, tmp_password)
			request.session['success'] = 'Superadmin created successfully!'
	return redirect('/admin/#users')

def delete_admin(request, admin_id):
	dbprint("DELETE ADMIN")
	return HttpResponse("Delete admin")

def login_view(request):
	if request.user.is_authenticated():
		return redirect('admin')
	if request.POST:
		email = request.POST.get('email', '').strip()
		password = request.POST.get('password', '').strip()
		user = authenticate(username=email, password=password)
		login_form = LoginForm(request.POST)
		if user and login_form.is_valid():
			login(request, user)
			return redirect('login_view')
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
			return redirect('/admin')
	login_form = LoginForm()
	return render(request, 'admin_custom/login.html', { 'login_form': login_form })

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
