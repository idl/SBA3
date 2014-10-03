from django.shortcuts import render, redirect
from ..models import AnswerSet, Student

def previous(request):
    pagenum = int(request.POST.get('pagenum', 1))
    # Redirect
    if pagenum <= 1:
        return redirect('page', 1)
    else:
        return redirect('page', pagenum - 1)

def next(request):
    print "\n\n--------DEBUG--------"
    pagenum = int(request.POST.get('pagenum', 1))
    # Get the answers and store them in the session
    array_name = "p" + str(request.POST.get('pagenum', 1))
    answer_array = request.POST.getlist(array_name + "[]")
    request.session[array_name] = answer_array
    print str(enumerate(request.session[array_name]))
    # Check for empty/blank fields
    for i in enumerate(request.session[array_name]):
        if i[1] == '':
            request.session['error'] = True
            return redirect('page', pagenum)
    # Redirect
    if pagenum >= 11:
        return redirect('page', 11)
    else:
        row = {}
        page = "p" + str(pagenum)
        try:
            current_student = Student.objects.filter(id=request.session['user_id']).get()
            answer_array = request.session[page]
            answernum = 1
            for answer in answer_array:
                column = page + "q" + str(answernum)
                row[column] = answer
                answernum = answernum + 1
            instance, created = AnswerSet.objects.get_or_create(student_id=current_student)
            for attr, value in row.iteritems(): 
                setattr(instance, attr, value)
            instance.save()
        except:
            return redirect('page', pagenum)
        return redirect('page', pagenum + 1)

def submit(request):
    array_name = "p11"
    answer_array = request.POST.getlist(array_name + "[]")
    request.session[array_name] = answer_array
    row = {}
    answer_array = []
    # Check for empty/blank fields
    for i in enumerate(request.session[array_name]):
        if i[1] == '':
            request.session['error'] = True
            # return redirect('page', pagenum)
    for pagenum in range(1,12):
        page = "p" + str(pagenum)
        try:
            answer_array = request.session[page]
        except:
            return redirect('page', pagenum)
        answernum = 1
        for answer in answer_array:
            column = page + "q" + str(answernum)
            row[column] = answer
            answernum = answernum + 1
    current_student = Student.objects.filter(id=request.session['user_id']).get()
    instance, created = AnswerSet.objects.get_or_create(student_id=current_student)
    for attr, value in row.iteritems(): 
        setattr(instance, attr, value)
    instance.save()
    setattr(current_student, 'completed', True)
    current_student.save()

    return redirect('report')

def save_survey(request):
    page_num = request.POST.get('pagenum','')
    if page_num != '':
        array_name = 'p' + str(page_num)
    else:
        request.session[save_error] = "incorrect page"
        return redirect('/')
    answer_array = request.POST.getlist(array_name + "[]")
    request.session[array_name] = answer_array
    row = {}
    answer_array = []
    for pagenum in range(1,12):
        page = "p" + str(pagenum)
        try:
            answer_array = request.session[page]
            answernum = 1
            for answer in answer_array:
                column = page + "q" + str(answernum)
                row[column] = answer
                answernum = answernum + 1
        except:
            pass
        
    current_student = Student.objects.filter(id=request.session['user_id']).get()
    instance, created = AnswerSet.objects.get_or_create(student_id=current_student)
    for attr, value in row.iteritems(): 
        setattr(instance, attr, value)
    instance.save()

    request.session.flush()
    return redirect('/#continue')

def report(request):
    current_student = Student.objects.filter(id=request.session['user_id']).get()
    row = AnswerSet.objects.values().filter(student_id=current_student).get()

    request.session.flush()
    return render(request, 'answers.html', {'row':row})