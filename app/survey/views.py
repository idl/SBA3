from django.shortcuts import render, redirect
from .forms.begin_survey_form import SurveyBeginForm
from .forms.questions_page_1 import QuestionsPage1Form

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
  context['questions_page_1_form'] = QuestionsPage1Form()
  return render(request, "survey/survey_questions.html", context)
