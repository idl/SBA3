from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.validators import EmailValidator
from django.contrib.auth import logout
from .forms import LoginForm

# Create your views here.
def admin_index(request):
	print request.user
	if request.user.is_authenticated():
		return HttpResponse("Is authenticated")
	else:
		# Best practice: Inside templates directory, always include subdirectory
		#                with same name as app (see templates dir). This helps with
		#				 template files with the same name of different apps.
		# https://docs.djangoproject.com/en/dev/howto/static-files/
		return redirect('')

def login_view(request):
	if request.POST:
		form = LoginForm(request.POST)
		msg = ""
		if form.is_valid():
			msg = "Valid"
		else:
			msg = "NOT Valid"
		return HttpResponse(msg)
	else:
		return redirect('')
	return HttpResponse("Logged into admin home")

def logout_view(request):
	logout(request)
	return HttpResponse("logged out")
