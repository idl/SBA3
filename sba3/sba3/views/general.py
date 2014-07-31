from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.loading import get_model


def questions(request):
   return render(request,'questions.html')

def page(request, pagenum):
    if pagenum=='1':
        return render(request, 'page1.html')
    elif pagenum=='2':
        return render(request, 'page2.html')
    elif pagenum=='3':
        return render(request, 'page3.html')
    elif pagenum=='4':
        return render(request, 'page4.html')
    elif pagenum=='5':
        return render(request, 'page5.html')
    elif pagenum=='6':
        return render(request, 'page6.html')
    elif pagenum=='7':
        return render(request, 'page7.html')
    elif pagenum=='8':
        return render(request, 'page8.html')
    elif pagenum=='9':
        return render(request, 'page9.html')
    elif pagenum=='10':
        return render(request, 'page10.html')
    elif pagenum=='11':
        return render(request, 'page11.html')
    else:
        return render(request, 'questions.html')