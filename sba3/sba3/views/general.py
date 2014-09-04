from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.loading import get_model

from ..forms import surveyLoginForm
from admin_custom.forms import LoginForm

def home(request):
    err_msg = request.session.get('err_msg', '')
    request.session['err_msg'] = ''
    return render(request, 'home.html', {'surveyLoginForm':surveyLoginForm, 'login_form':LoginForm, 'err_msg': err_msg})

def questions(request):
   return render(request,'questions.html')

def page(request, pagenum):
    error = request.session.get('error', False)
    request.session['error'] = False
    # print '\n\n',request.POST.lists(),'\n\n'
    ctx = {'pagenum': pagenum, 'error': error}
    if pagenum=='1':
        return render(request, 'page1.html', ctx)
    print("******************** " + pagenum)
    if pagenum=='1':
        return render(request, 'page1.html', {'pagenum': 5, 'error': error})
    elif pagenum=='2':
        if 'p1' in request.session:
            return render(request, 'page2.html', ctx)
        else:
            return redirect('page', 1)
    elif pagenum=='3':
        if 'p2' in request.session:
            return render(request, 'page3.html', ctx)
        else:
            return redirect('page', 2)
    elif pagenum=='4':
        if 'p3' in request.session:
            return render(request, 'page4.html', ctx)
        else:
            return redirect('page', 3)
    elif pagenum=='5':
        if 'p4' in request.session:
            return render(request, 'page5.html', ctx)
        else:
            return redirect('page', 4)
    elif pagenum=='6':
        if 'p5' in request.session:
            return render(request, 'page6.html', ctx)
        else:
            return redirect('page', 5)
    elif pagenum=='7':
        if 'p6' in request.session:
            return render(request, 'page7.html', ctx)
        else:
            return redirect('page', 6)
    elif pagenum=='8':
        if 'p7' in request.session:
            return render(request, 'page8.html', ctx)
        else:
            return redirect('page', 7)
    elif pagenum=='9':
        if 'p8' in request.session:
            return render(request, 'page9.html', ctx)
        else:
            return redirect('page', 8)
    elif pagenum=='10':
        if 'p9' in request.session:
            return render(request, 'page10.html', ctx)
        else:
            return redirect('page', 9)
    elif pagenum=='11':
        if 'p10' in request.session:
            return render(request, 'page11.html', ctx)
        else:
            return redirect('page', 10)
    else:
        return redirect('page', 11)

def login_view(request):
	return redirect('admin_custom.views.login_view')

def logout_view(request):
	return redirect('admin_custom.views.logout_view')

def clearSession(request):
    request.session.flush()
    return redirect('/admin')
    
