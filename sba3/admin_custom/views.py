from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.validators import EmailValidator
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .forms import LoginForm, registerAdminForm, registerSchoolUserForm

from sba3.models import School

Users = get_user_model()

@login_required(redirect_field_name='')
def admin(request):
	err_msg = request.session.get('err_msg', '')
	request.session['err_msg'] = ''
	success = request.session.get('success', '')
	request.session['success'] = ''
	# if username param in url doesn't match an actual username, redirect to 'login_view'
	regsiterAdminForm = registerAdminForm()
	registerError = request.session.get('registerError', False)
	request.session['registerError'] = False
	registerSuccess = request.session.get('registerSuccess', False)
	request.session['registerSuccess'] = False
	regsiterSchoolUserForm = registerSchoolUserForm()

	school_list = School.objects.all()
	superadmin_list = Users.objects.filter(is_superuser=True)
	schooladmin_list = []
	for user in Users.objects.filter(is_superuser=False).order_by('school_id'):
		schooladmin_entry = {}
		# schooladmin_entry[]
		dbprint(user.email)
		schooladmin_entry['id'] = user.id
		schooladmin_entry['email'] = user.email
		schooladmin_entry['school'] = School.objects.get(id=user.school_id)
		schooladmin_entry['last_login'] = user.last_login
		schooladmin_entry['date_joined'] = user.date_joined
		schooladmin_list.append(schooladmin_entry)
	dbprint(schooladmin_list)
	ctx = { 'registerAdminForm': regsiterAdminForm,
			'err_msg': err_msg,
			'success': success,
			'registerSchoolUserForm': regsiterSchoolUserForm,
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
	# School.objects.all().delete()
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
	print School.objects.values('name').all()
	return HttpResponseRedirect(reverse('admin') + '#registerschools')

@login_required
def register_admin(request):
	if request.POST:
		email = request.POST.get('email', '')
		password = request.POST.get('password', '')
		password_confirm = request.POST.get('password_confirm', '')
		school_id = request.POST.get('school', None)
		err_msg = ''

		if email == '' and password == '':
			err_msg = 'Email and password fields cannot be blank.'
		elif email == '':
			err_msg = 'Email cannot be blank.'
		elif password == '':
			err_msg = 'Password cannot be blank.'
		elif password != password_confirm:
			err_msg = 'Passwords must match'

		reg_form = registerAdminForm(request.POST)
		
		if not reg_form.is_valid():
			err_msg = 'Error in the form'

		try:
			Users.objects.get(email=email)
			err_msg = 'Email address in use'
		except:
			if request.POST.get('superuser', False) == False:
				Users.objects.create_user(email, password, school_id)
				request.session['success'] = 'User Created Successfully'
			else:
				Users.objects.create_superuser(email, password)
				request.session['success'] = 'Superuser Created Successfully'

		if err_msg != '':
			request.session['err_msg'] = err_msg
			return redirect('/admin#users')
	return redirect('/admin#users')

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
			err_msg = "Email and password combination doesn't match database records. Please try logging in again."
			if email == '' and password == '':
				err_msg = 'Email and password fields cannot be blank.'
			elif email == '':
				err_msg = 'Email cannot be blank.'
			elif password == '':
				err_msg = 'Password cannot be blank.'
			# return render(request, 'home.html', { 'login_form': login_form, 'err_msg': err_msg })
			request.session['err_msg'] = err_msg
			return redirect('/#login')
	login_form = LoginForm()
	return redirect('/#login')

@login_required(redirect_field_name='')
def logout_view(request):
	logout(request)
	return redirect('home')

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
