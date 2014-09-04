from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.core.validators import EmailValidator
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, registerSchoolUserForm

SurveyUser = get_user_model()

@login_required(redirect_field_name='')
def admin(request):
	# if username param in url doesn't match an actual username, redirect to 'login_view'
	regsiterSchoolUserForm = registerSchoolUserForm()
	return render(request, 'admin_custom/admin.html', { 'registerSchoolUserForm': regsiterSchoolUserForm })


@login_required(redirect_field_name='')
def create_user(request):
	dbprint('in create user')
	return HttpResponse("test response")


def login_view(request):
	# if request.user.email != '':
	# 	uid = request.session['_auth_user_id']
	# 	uname = SurveyUser.objects.get(id=uid).email
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
			return render(request, 'admin_custom/login.html', { 'login_form': login_form, 'err_msg': err_msg })
	login_form = LoginForm()
	return render(request, 'admin_custom/login.html', { 'login_form': login_form })

@login_required(redirect_field_name='')
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
