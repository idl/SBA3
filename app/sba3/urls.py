from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from admin import views as AdminViews
from survey import views as SurveyViews
from . import views as Sba3Views


urlpatterns = [
  url(r'^$', Sba3Views.public_index, name='public_index'),

  url(r'^admin/login$', AdminViews.public_login, name='public_admin_login'),

  url(r'^survey/(?P<school_id>\d{1,3})/(?P<student_uid>[a-z0-9]{1,24})/page/(?P<page_num>\d{1,2})$', SurveyViews.questions, name='survey_questions'),
  url(r'^survey/begin$', SurveyViews.public_begin, name='public_survey_begin'),
  url(r'^survey/continue$', SurveyViews.public_continue, name='public_survey_continue'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
