from django.shortcuts import render, redirect
from django.contrib import messages

########################
### messages example ###
########################
  # # explicitly add info tag -- default bootstrap class doesn't work
  # messages.info(request, 'Hello world.', extra_tags='info')
  # messages.error(request, 'Hello world.')
  # messages.warning(request, 'Hello world.')
  # messages.success(request, 'Hello world.')

def public_index(request):
  return render(request, "public/index.html")
