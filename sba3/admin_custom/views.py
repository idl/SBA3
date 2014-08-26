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
def admin_index(request):
	print "At admin_index view"
	login(request, authenticate(username="admin", password="admin"))
	if not request.user.is_authenticated():
		dbprint("Not authenticated. Redirecting to admin_custom.views.login_view")
		return redirect('admin_custom.views.login_view')

def login_view(request):
	print authenticate(username="admin", password="admin")
	if request.user.is_authenticated():
		dbprint("User is logged in. Redirecting to admin_custom.views.admin_index")
		return redirect('admin_custom.views.admin_index')

	if request.POST:
		email = request.POST['email'].strip()
		password = request.POST['password'].strip()
		user = authenticate(username=email, password=password)
		if user:
			dbprint("Authenticated!!!")
		else:
			dbprint("Not authenticated!!!")
	return render(request, 'admin_custom/login.html')

def logout_view(request):
	logout(request)
	return redirect('admin_custom.views.login_view')
