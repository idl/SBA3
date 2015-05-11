import json
from collections import OrderedDict as ODict
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
from .models import Student, School, Uid, ResultSet
from django.contrib.auth.decorators import user_passes_test

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
  '1': 11,
  '2': 11,
  '3': 9,
  '4': 11,
  '5': 11,
  '6': 12,
  '7': 9,
  '8': 12,
  '9': 11,
  '10': 12,
  '11': 14,
  'total': 123
}

num_questions_so_far = {
  '1': 0,
  '2': 11,
  '3': 22,
  '4': 31,
  '5': 42,
  '6': 56,
  '7': 68,
  '8': 77,
  '9': 89,
  '10': 102,
  '11': 114
}

def public_continue(request):
  return render(request, "survey/survey_continue.html")

def questions(request, school_id, student_uid, page_num):
  context = {}

  if int(page_num) > 11 or int(page_num) < 1:
    return redirect('survey_questions', school_id, student_uid, 11)

  if int(page_num) is not 1:
    rs = Student.objects.filter(
      school__id=school_id,
      uid=Uid.objects.get(uid=student_uid)
    ).get().result_set
    if getattr(rs, 'p'+str(page_num)) is None:
      return redirect('survey_questions', school_id, student_uid, int(page_num)-1)
    for q_num in range(1, num_questions_on_page[page_num]+1):
      if json.loads(getattr(rs, 'p'+str(page_num)))['q'+str(q_num)] is None:
        return redirect('survey_questions', school_id, student_uid, int(page_num)-1)

  # student can only access the survey with their own credentials which are set
  # in the session when they begin survey
  if request.session.get('student_uid') != student_uid or request.session.get('school_id') != int(school_id):
    messages.error(request, 'Could not process your request.')
    return redirect('public_survey_begin')

  try:
    school = School.objects.get(id=school_id)
    uid = Uid.objects.get(uid=student_uid)
    Student.objects.get(school=school, uid=uid)
  except:
    messages.error(request, 'Could not process your request.')
    return redirect('public_survey_begin')

  if request.POST:
    form = forms[page_num](request.POST)
    if form.is_valid():
      request.session['next_page_num'] = int(page_num) + 1
    else:
      messages.error(request, 'You must answer all of the questions on the page before continuing.')
      request.session['next_page_num'] = page_num
    for q_num in range(1, num_questions_on_page[page_num]+1):
      request.session['page_results_q'+str(q_num)] = request.POST.get('q'+str(q_num))
    return redirect('survey_next')
  context['student_uid'] = student_uid
  context['school_id'] = school_id
  context['questions_page_form'] = forms[page_num]()
  context['page_num'] = int(page_num)
  context['previous_page_num'] = int(page_num)-1
  try:
    context['progress_percentage'] = "%0.0f" % (float(num_questions_so_far[page_num])/num_questions_on_page['total'] * 100)
  except:
    context['progress_percentage'] = 0
  return render(request, "survey/survey_questions.html", context)

def next(request):
  next_page_num = int(request.session.get('next_page_num'))
  school_id = request.session.get('school_id')
  student_uid = request.session.get('student_uid')
  if next_page_num is 1:
    return redirect('survey_questions', school_id, student_uid, next_page_num)
  student = Student.objects.filter(
    school__id=school_id,
    uid=Uid.objects.get(uid=student_uid)
  ).get()
  rs = student.result_set
  res_set_tmp = {}
  for q_num in range(1, num_questions_on_page[str(next_page_num-1)]+1):
    res_set_tmp['q'+str(q_num)] = request.session.get('page_results_q'+str(q_num))
  setattr(rs, 'p'+str(next_page_num-1), json.dumps(res_set_tmp))
  rs.save()
  return redirect('survey_questions', school_id, student_uid, next_page_num)

def previous(request):
  return redirect('survey_questions')

def clear(request):
  request.session.flush()
  return HttpResponse("session cleared")

def public_begin(request):
  context = {}
  context['survey_begin_form'] = SurveyBeginForm()
  if request.POST:
    form = SurveyBeginForm(request.POST)
    if not form.is_valid():
      messages.error(request, 'You must pick a school and enter your student identifier to take the survey.')
      return render(request, "survey/survey_begin.html", context)
    school_id = int(request.POST.get('school'))
    student_uid = request.POST.get('student_uid')
    context['school_id'] = school_id
    context['survey_begin_form'] = form
    student = None
    try:
      student = Student.objects.get(
        uid=Uid.objects.get(uid=student_uid),
        school=School.objects.get(id=school_id))
    except:
      messages.error(request,
        'The user ID "'+student_uid+'" is not registered with this school.')
      return render(request, "survey/survey_begin.html", context)
    if student.completed:
      messages.error(request, 'The student "'+student_uid+'" has already completed the survey.')
      return render(request, "survey/survey_begin.html", context)
    if student.has_started_survey():
      messages.error(request, 'The student "'+student_uid+'" has already started the survey. Please click the "Go Back" button and choose the "Continue Survey')
      return render(request, "survey/survey_begin.html", context)
    request.session['student_uid'] = student_uid
    request.session['school_id'] = school_id
    result_set = None
    if student.result_set is None:
      result_set = ResultSet()
      for page_num in range(1, 12):
        res_set_outline = {}
        for q_num in range(1, num_questions_on_page[str(page_num)]+1):
          res_set_outline['q'+str(q_num)] = None
        # result_set.p+str(page_num) = json.dumps(res_set_outline)
        setattr(result_set, 'p'+str(page_num), json.dumps(res_set_outline))
      result_set.save()
      student.result_set = result_set
    student.save()
    return redirect('survey_questions', school_id, student_uid, 1)
  return render(request, "survey/survey_begin.html", context)

