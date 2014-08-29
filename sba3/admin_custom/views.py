from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.validators import EmailValidator
from django.contrib.auth import login, logout, authenticate

def dbprint(input_str):
	input_str = str(input_str)
	output_str = "\n\n"
	output_str += "#" * (len(input_str) + 4)
	output_str += "\n"
	output_str += "  " + input_str.strip()
	output_str += "\n"
	output_str += "#" * (len(input_str) + 4)
	output_str += "\n\n"
	print output_str

# Create your views here.
def admin_home(request):
	is_authenticated = request.user.is_authenticated()
	dbprint("Authenticated? " + str(is_authenticated))
	if not is_authenticated:
		return redirect('admin_custom.views.login_view')
	return render(request, 'admin_custom/admin_home.html', { "is_authenticated": is_authenticated})

def login_view(request):
	if request.user.is_authenticated():
		return redirect('admin_custom.views.admin_home')

	if request.POST:
		email = request.POST['email'].strip()
		password = request.POST['password'].strip()
		user = authenticate(username=email, password=password)
		if user:
			login(request, user)
			dbprint("Authenticated. Redirecting to admin_home")
			return redirect('admin_custom.views.admin_home')
		else:
			dbprint("Not authenticated. Reloading")
			return render(request, 'admin_custom/login.html', { 'login_err': True})
	return render(request, 'admin_custom/login.html')

def logout_view(request):
	logout(request)
	return redirect('admin_custom.views.login_view')
