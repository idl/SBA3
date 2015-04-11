from django.shortcuts import render, redirect
from django.contrib import messages
# import pprint

def public_index(request):

  # explicitly add info tag -- default bootstrap class doesn't work
  messages.info(request, 'Hello world.', extra_tags='info')
  return render(request, "public/index.html", dirs=('sba3/templates/',))