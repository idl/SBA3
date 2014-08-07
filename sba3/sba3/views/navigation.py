from django.shortcuts import render, redirect
from ..models import Answers

def previous(request):
    pagenum = int(request.POST.get('pagenum', 1))

    # Get the answers and store them in the session
    array_name = "p" + request.POST.get('pagenum', 1)
    answer_array = request.POST.getlist(array_name + "[]")
    request.session[array_name] = answer_array

    # Redirect
    if pagenum <= 1:
        return redirect('page', 1, test= 'test')
    else:
        return redirect('page', pagenum - 1)

def next(request):
    pagenum = int(request.POST.get('pagenum', 1))

    # Get the answers and store them in the session
    array_name = "p" + request.POST.get('pagenum', 1)
    answer_array = request.POST.getlist(array_name + "[]")
    request.session[array_name] = answer_array
    for i in range(len(answer_array)):
        print str(i)+": "+answer_array[i]

    # Redirect
    if pagenum >= 11:
        return redirect('page', 11)
    else:
        return redirect('page', pagenum + 1)

def submit(request):
    array_name = "p11"
    answer_array = request.POST.getlist(array_name + "[]")
    request.session[array_name] = answer_array

    row = {}

    for pagenum in range(1,12):
        page = "p" + str(pagenum)
        answer_array = request.session[page]
        answernum = 1
        for answer in answer_array:
            column = page + "q" + str(answernum)
            row[column] = answer
            answernum = answernum + 1

    print row

    submission = Answers(**row)
    submission.save()

    request.session.flush()

    return render(request, 'questions.html')