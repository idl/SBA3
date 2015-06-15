from django.shortcuts import render, redirect
from django.contrib import messages

# public index view
def public_index(request):
  return render(request, "public/index.html")

