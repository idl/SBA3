import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.http import urlencode
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
from django.utils import timezone as tz
from .forms.begin_survey_form import SurveyBeginForm
from .forms.continue_survey_form import SurveyContinueForm
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
from .models import Student, School, ResultSet
from .constants import num_questions_on_page, num_questions_so_far
from .conditions import add_condition_questions_to_session


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


def questions(request, school_id, student_uid, page_num):
  context = {}

  if int(page_num) > 11 or int(page_num) < 1:
    return redirect('survey_questions', school_id, student_uid, 11)

  # student can only access the survey with their own credentials which are set
  # in the session when they begin survey
  if request.session.get('student_uid') != student_uid or request.session.get('school_id') != int(school_id):
    print "SESSION DOESNT MATCH STUDENT"
    messages.error(request, 'Could not process your request.')
    return redirect('public_survey_begin')

  student = Student.objects.filter(school__id=school_id,uid=student_uid).get()

  if student.has_completed_survey_for_current_year():
    messages.error(request, 'The student "'+student_uid+'" has already completed the survey.')
    return redirect('public_survey_begin')

  rs = student.get_result_set_for_current_year()

  # if this page has questions that haven't been answered, redirect to
  # the previous page (unless the previous page's questions ALL have
  # been answered)
  if int(page_num) > 1 and not rs.all_questions_answered(page_num):
    if not rs.all_questions_answered(int(page_num)-1):
      return redirect('survey_questions', school_id, student_uid, int(page_num)-1)

  try:
    school = School.objects.get(id=school_id)
    Student.objects.get(school=school, uid=student_uid)
  except:
    messages.error(request, 'Could not process your request.')
    return redirect('public_survey_begin')

  if request.method == 'POST':
    form = forms[page_num](post_data=request.POST)
    request.session['next_page_num'] = int(page_num) + 1

    # if student didnt answer all of the questions, not counting the ones that
    # arent visible because they are skipped, show err msg
    for q_num in range(1, num_questions_on_page[page_num]+1):
      request.session['page_results_q'+str(q_num)] = request.POST.get('q'+str(q_num))
    if not form.is_valid():
      messages.error(request, 'You must answer all of the questions on the page before continuing.')
      for q_num in range(1, num_questions_on_page[page_num]+1):
        request.session['page_results_q'+str(q_num)] = None
    return redirect('survey_next')
  if rs.all_questions_answered(page_num):
    res_set = json.loads(getattr(rs, 'p'+str(page_num)))
    context['questions_page_form'] = forms[page_num](post_data=res_set, session=request.session)
  else:
    context['questions_page_form'] = forms[page_num](session=request.session)
  context['survey_title'] = school.survey_title or None
  context['student_uid'] = student_uid
  context['school_id'] = school_id
  context['school_name'] = student.school.name
  context['num_questions_on_page'] = num_questions_on_page[page_num]
  context['page_num'] = int(page_num)
  context['previous_page_num'] = int(page_num)-1
  context['continue_pass'] = student.continue_pass
  if request.session.get('show_modal') and int(page_num) is 1:
    context['show_modal'] = True
    del request.session['show_modal']
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
  student = Student.objects.filter(school__id=school_id,uid=student_uid).get()
  rs = student.get_result_set_for_current_year()
  res_set_tmp = {}
  for q_num in range(1, num_questions_on_page[str(next_page_num-1)]+1):
    ans = request.session.get('page_results_q'+str(q_num))
    res_set_tmp['q'+str(q_num)] = ans
  json_res_set = json.dumps(res_set_tmp)
  add_condition_questions_to_session(res_set_tmp, next_page_num-1, request.session)
  setattr(rs, 'p'+str(next_page_num-1), json_res_set)
  rs.save()
  if next_page_num == 12:
    rs.completed = True
    rs.save()
    student.save()
    return redirect('survey_results', school_id, student_uid, tz.now().year)
  return redirect('survey_questions', school_id, student_uid, next_page_num)


def results(request, school_id, student_uid, survey_year):
  context = {}

  if request.user.is_authenticated():
    context['is_admin'] = True
    if not request.user.is_superuser:
      # if
      if int(school_id) != request.user.school.id:
        print 'school doesnt match'
        messages.error(request, 'Could not process your request.')
        return redirect('admin_school_overview', school_id=request.user.school.id)
  else:
    # student can only access the survey with their own credentials which are set
    # in the session when they begin survey
    if request.session.get('student_uid') != student_uid or request.session.get('school_id') != int(school_id):
      print 'sessions dont match'
      messages.error(request, 'Could not process your request.')
      return redirect('public_index')
  student = None
  try:
    school = School.objects.get(id=school_id)
    student = Student.objects.get(school=school, uid=student_uid)
  except:
    print 'school or student not found'
    messages.error(request, 'Could not process your request.')
    return redirect('public_index')

  rs = student.get_result_set_for_year(survey_year)
  if not rs:
    if request.user.is_authenticated():
      return redirect('admin_school_overview', school_id=school_id, survey_year=survey_year)
    else:
      messages.error(request, 'Could not process your request.')
      return redirect('public_index')

  full_rs = {}

  for page_num in range(1, 11+1):
    pg_rs = json.loads(getattr(rs, 'p'+str(page_num)))
    full_rs['p'+str(page_num)] = pg_rs
    context['form_page_'+str(page_num)] = forms[str(page_num)](post_data=pg_rs)

  def getans(page_num, q_num):
    return full_rs['p'+str(page_num)]['q'+str(q_num)]

  if rs.completed:
    q_44 = {
      'strongdisagree': 1.0,
      'disagree': 2.0,
      'neutral': 3.0,
      'agree': 4.0,
      'strongagree': 5.0
    }
    q_36 = {
      'a': 4.0,
      'b': 3.0,
      'c': 2.0,
      'd': 1.0,
      'f': 0.0
    }
    q_26 = {
      'never': 1.0,
      'rarely': 2.0,
      'some': 3.0,
      'often': 4.0
    }

    # calculate track_college_readiness
    def calc_track_college_readiness():
      mean_q = [getans(8,6),getans(8,7),getans(8,8),getans(8,9),getans(8,10),getans(8,11),getans(8,12)]
      if None not in mean_q:
        mean = 0.0
        for ans in mean_q:
          if ans not in q_44:
            # did not answer enough questions to receive feedback
            return None
        for ans in mean_q:
          mean += q_44[ans]
        return mean/float(len(mean_q))
      return None

    # calculate track_self_concept
    def calc_track_self_concept():
      mean_q = [getans(7,2),getans(7,3),getans(7,4),getans(7,5)]
      if None not in mean_q:
        mean = 0.0
        for ans in mean_q:
          if ans not in q_36:
            # did not answer enough questions to receive feedback
            return None
        for ans in mean_q:
          mean += q_36[ans]
        return mean/float(len(mean_q))
      return None

    # calculate track_self_efficacy
    def calc_track_self_efficacy():
      mean_q = [getans(7,1)]
      if None not in mean_q:
        mean = 0.0
        for ans in mean_q:
          if ans not in q_36:
            # did not answer enough questions to receive feedback
            return None
        for ans in mean_q:
          mean += q_36[ans]
        return mean/float(len(mean_q))
      return None

    # calculate track_socioeconomic_status
    def calc_track_socioeconomic_status():
      q27_6 = getans(4,6)
      q27_9 = getans(4,9)
      if q27_6 == 'no' or q27_9 == 'no':
        return True
      return None

    # calculate track_academic_behaviors
    def calc_track_academic_behaviors():
      q20 = getans(2,11)
      try:
        return int(q20)
      except:
        return None
      return None

    # calculate track_risky_behaviors
    def calc_track_risky_behaviors():
      q26_1 = getans(3,6)
      q26_2 = getans(3,7)
      q26_3 = getans(3,8)
      if q26_1 == None or q26_1 not in q_26:
        return None
      if q26_2 == None or q26_2 not in q_26:
        return None
      if q26_3 == None or q26_3 not in q_26:
        return None

      q26_1 = q_26[q26_1]
      q26_2 = q_26[q26_2]
      q26_3 = q_26[q26_3]

      mean = (q26_1+q26_2+q26_3)/3.0
      return mean


    context['track_college_readiness'] = calc_track_college_readiness()
    context['track_self_concept'] = calc_track_self_concept()
    context['track_self_efficacy'] = calc_track_self_efficacy()
    context['track_socioeconomic_status'] = calc_track_socioeconomic_status()
    context['track_academic_behaviors'] = calc_track_academic_behaviors()
    context['track_risky_behaviors'] = calc_track_risky_behaviors()
  context['student_uid'] = student_uid
  context['school_id'] = school_id
  context['student_completed'] = rs.completed
  return render(request, "survey/survey_results.html", context)


def clear(request):
  request.session.flush()
  return HttpResponse("""
    <html><head>
    <meta http-equiv=\"refresh\" content=\"0.5;URL='/survey/begin'\" />
    </head><body>session cleared</body></html>
    """)


def public_begin(request):
  context = {}
  context['survey_begin_form'] = SurveyBeginForm()
  if request.method == 'POST':
    form = SurveyBeginForm(request.POST)
    if not form.is_valid():
      messages.error(request, 'You must pick a school and enter your student identifier to take the survey.')
      return render(request, "survey/survey_begin.html", context)
    school_id = int(request.POST.get('school'))
    student_uid = request.POST.get('student_uid')
    context['school_id'] = school_id
    context['survey_begin_form'] = form
    student = None
    try:student = Student.objects.get(uid=student_uid,school=School.objects.get(id=school_id))
    except:
      messages.error(request,
        'The user ID "'+student_uid+'" is not registered with this school.')
      return render(request, "survey/survey_begin.html", context)
    if student.has_completed_survey_for_current_year():
      messages.error(request, 'The student "'+student_uid+'" has already completed the survey.')
      return render(request, "survey/survey_begin.html", context)
    if student.has_started_survey_for_current_year():
      messages.error(request, 'The student "'+student_uid+'" has already started the survey. <a href="/survey/continue" style="color:white;text-decoration:underline;font-weight:700;">Click here to continue the survey</a>.')
      return render(request, "survey/survey_begin.html", context)
    request.session.flush()
    request.session['student_uid'] = student_uid
    request.session['school_id'] = school_id
    request.session['show_modal'] = True
    result_set = None
    if student.get_result_set_for_current_year() == None:
      result_set = ResultSet(student=student)
      for page_num in range(1, 12):
        res_set_outline = {}
        for q_num in range(1, num_questions_on_page[str(page_num)]+1):
          res_set_outline['q'+str(q_num)] = None

        # equivalent:
        # result_set.p+str(page_num) = json.dumps(res_set_outline)
        setattr(result_set, 'p'+str(page_num), json.dumps(res_set_outline))
      result_set.save()
      student.result_set = result_set
    student.save()
    # try:
    url = "localhost:8000/survey/continue?continue_pass="+student.continue_pass+"&school="+str(student.school.id)+"&student_uid="+student.uid
    msg = str("You have begun the SBA<sup>3</sup>-1 Survey. Please click the following link to continue the survey where you left off:<br> "+
      "<a href='" + url + "'>" + url + "</a>" +
      "<br><br>Your information is as follows:<br><ul>" +
      "<li><b>Student Identifier</b>: " + student.uid + "</li>" +
      "<li><b>School</b>: " + student.school.name + "</li>" +
      "<li><b>Continuation Passkey</b>: " + student.continue_pass + "</li></ul>")
    send_mail("SBA3-1 Survey - Continuation Key",
      "",
      'sba3survey@msussrc.com', [student.email],
      fail_silently=False, html_message=msg)
    return redirect('survey_questions', school_id, student_uid, 1)
  return render(request, "survey/survey_begin.html", context)


def public_continue(request):
  # form.is_valid() is false only when it contains a blank field
  #   - more processing required to determine if the CREDENTIALS are valid
  context = {}
  context['survey_continue_form'] = SurveyContinueForm()
  if request.GET:
    continue_pass = request.GET.get('continue_pass')
    student_uid = request.GET.get('student_uid')
    school_id = int(request.GET.get('school'))
    if continue_pass and student_uid and school_id:
      form = SurveyContinueForm({
          'school': school_id,
          'continue_pass': continue_pass,
          'student_uid': student_uid
        })
      if form.is_valid():
        student = None
        try:student = Student.objects.get(uid=student_uid,school=School.objects.get(id=school_id))
        except:
          messages.error(request,
            'The user ID "'+student_uid+'" is not registered with this school.')
          return render(request, "survey/survey_continue.html", context)
        if student.has_completed_survey_for_current_year():
          messages.error(request,
            'The student "'+student_uid+'" has already completed the survey.')
          return render(request, "survey/survey_continue.html", context)
        if not student.has_started_survey_for_current_year():
          messages.error(request,
            'The student "'+student_uid+'" has not started the survey. <a href="/survey/begin" style="color:white;text-decoration:underline;font-weight:700;">Click here to begin the survey</a>.')
          return render(request, "survey/survey_continue.html", context)
        if continue_pass != student.continue_pass:
          messages.error(request,
            'The continuation passkey does not match the student "<span style="text-decoration:underline;font-weight:700;">'+student_uid+'</span>" at <span style="text-decoration:underline;font-weight:700;">'+student.school.name+'</span>.')
          return render(request, "survey/survey_continue.html", context)
        request.session.flush()
        request.session['student_uid'] = student_uid
        request.session['school_id'] = school_id
        return redirect('survey_questions', school_id, student_uid, 11)
  if request.method == 'POST':
    continue_pass = request.POST.get('continue_pass')
    student_uid = request.POST.get('student_uid')
    school_id = int(request.POST.get('school'))
    form = SurveyContinueForm(request.POST)
    if form.is_valid():
      student = None
      try:
        student = Student.objects.get(uid=student_uid,school=School.objects.get(id=school_id))
      except:
        messages.error(request,
          'The user ID "'+student_uid+'" is not registered with this school.')
        return render(request, "survey/survey_continue.html", context)
      if student.has_completed_survey_for_current_year():
        messages.error(request,
          'The student "'+student_uid+'" has already completed the survey.')
        return render(request, "survey/survey_continue.html", context)
      if not student.has_started_survey_for_current_year():
        messages.error(request,
          'The student "'+student_uid+'" has not started the survey. <a href="/survey/begin" style="color:white;text-decoration:underline;font-weight:700;">Click here to begin the survey</a>.')
        return render(request, "survey/survey_continue.html", context)
      if continue_pass != student.continue_pass:
        messages.error(request,
          'The continuation passkey does not match the student "<span style="text-decoration:underline;font-weight:700;">'+student_uid+'</span>" at <span style="text-decoration:underline;font-weight:700;">'+student.school.name+'</span>.')
        return render(request, "survey/survey_continue.html", context)
      request.session.flush()
      request.session['student_uid'] = student_uid
      request.session['school_id'] = school_id
      return redirect('survey_questions', school_id, student_uid, 11)
    else:
      messages.error(request, "Please enter all fields.")
  return render(request, "survey/survey_continue.html", context)



