from django.shortcuts import render

# Create your views here.
def admin_index(request):
	# Best practice: Inside templates directory, always include subdirectory
	#                with same name as app (see templates dir). This helps with
	#				 template files with the same name of different apps.
	# https://docs.djangoproject.com/en/dev/howto/static-files/
	return render(request, 'admin_custom/login.html')

def login(request):
	return render(request, 'admin_custom/login.html')

def logout(request):
	return render(request, 'admin_custom/login.html')

