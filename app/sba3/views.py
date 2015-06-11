from django.shortcuts import render, redirect
from django.contrib import messages

def public_index(request):
  return render(request, "public/index.html")

