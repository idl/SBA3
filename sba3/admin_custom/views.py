from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.validators import EmailValidator
from django.contrib.auth import logout
from .forms import LoginForm

# Create your views here.
def admin_index(request):
	print "At admin_index view"
	if request.user.is_authenticated():
		return HttpResponse("Is authenticated")
	else:
		return redirect('admin_custom.views.login_view')

def login_view(request):
	form = LoginForm(request.POST)
	return render(request, 'admin_custom/login.html', {'form': form})

def logout_view(request):
	logout(request)
	return HttpResponse("logged out")
