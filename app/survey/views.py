from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms.begin_survey_form import SurveyBeginForm
from .forms.questions_page_1 import QuestionsPage1Form
from .forms.questions_page_2 import QuestionsPage2Form
from .forms.questions_page_3 import QuestionsPage3Form
from .forms.questions_page_4 import QuestionsPage4Form
from .forms.questions_page_5 import QuestionsPage5Form
from .forms.questions_page_6 import QuestionsPage6Form
from .forms.questions_page_7 import QuestionsPage7Form
from .forms.questions_page_8 import QuestionsPage8Form
from .forms.questions_page_9 import QuestionsPage9Form
from .forms.questions_page_10 import QuestionsPage10Form
from .forms.questions_page_11 import QuestionsPage11Form

forms = {
  '1': QuestionsPage1Form,
  '2': QuestionsPage2Form,
  '3': QuestionsPage3Form,
  '4': QuestionsPage4Form,
  '5': QuestionsPage5Form,
  '6': QuestionsPage6Form,
  '7': QuestionsPage7Form,
  '8': QuestionsPage8Form,
  '9': QuestionsPage9Form,
  '10': QuestionsPage10Form,
  '11': QuestionsPage11Form,
}

num_questions_on_page = {
  'p1': 11,
  'p2': 11,
  'p3': 9,
  'p4': 11,
  'p5': 14,
  'p6': 12,
  'p7': 9,
  'p8': 12,
  'p9': 13,
  'p10': 12,
  'p11': 14,
  'total': 128
}

num_questions_so_far = {
  'p2': 11,
  'p3': 22,
  'p4': 31,
  'p5': 42,
  'p6': 56,
  'p7': 68,
  'p8': 77,
  'p9': 89,
  'p10': 102,
  'p11': 114
}

def public_begin(request):
  context = {}
  if request.POST:
    return redirect('survey_questions', school_id=1, student_uid="jgb221", page_num=1)
  else:
    context['survey_begin_form'] = SurveyBeginForm()
  return render(request, "survey/survey_begin.html", context)

def public_continue(request):
  return render(request, "survey/survey_continue.html")

def questions(request, school_id, student_uid, page_num):
  context = {}
  if request.POST:
    form = forms[page_num](request.POST)
    request.session['school_id'] = school_id
    request.session['student_uid'] = student_uid
    if form.is_valid():
      request.session['next_page_num'] = int(page_num) + 1
    else:
      messages.error(request, 'You must answer all of the questions on the page before continuing.')
      request.session['page_results'] = {}
      request.session['next_page_num'] = page_num
    for q_num in range(1, num_questions_on_page['p'+str(page_num)]+1):
      request.session['page_results']['q'+str(q_num)] = request.POST.get('q'+str(q_num))
    return redirect('survey_next')
  context['student_uid'] = student_uid
  context['school_id'] = school_id
  context['questions_page_form'] = forms[page_num]()
  context['previous_page_num'] = int(page_num)-1
  try:
    context['progress_percentage'] = "%0.0f" % (float(num_questions_so_far['p'+page_num])/num_questions_on_page['total'] * 100)
  except:
    context['progress_percentage'] = 0
  return render(request, "survey/survey_questions.html", context)

def next(request):
  next_page_num = request.session.get('next_page_num')
  school_id = request.session.get('school_id')
  student_uid = request.session.get('student_uid')
  print "page results: ", request.session.get('page_results')
  return redirect('survey_questions', school_id, student_uid, next_page_num)

def previous(request):
  return redirect('survey_questions')

def clear(request):
  request.session.flush()
  return HttpResponse("session cleared")

