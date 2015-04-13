from django.shortcuts import render, redirect
from .forms import AdminLoginForm

def public_login(request):
  context = {
    'admin_login_form': AdminLoginForm(),
  }
  return render(request, "admin/public_login.html", context)
