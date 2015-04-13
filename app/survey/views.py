from django.shortcuts import render, redirect
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
  '11': QuestionsPage10Form,
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
  context['page_num'] = int(page_num)
  context['student_uid'] = student_uid
  context['questions_page_form'] = forms[page_num]()
  return render(request, "survey/survey_questions.html", context)
