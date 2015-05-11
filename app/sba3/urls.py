from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from admin_custom import urls as AdminUrls
from survey import views as SurveyViews
from . import views as Sba3Views


urlpatterns = [
  url(r'^$', Sba3Views.public_index, name='public_index'),
  url(r'^admin/', include(AdminUrls)),
  url(r'^survey/(?P<school_id>\d{1,3})/(?P<student_uid>[A-Za-z0-9]{1,24})/page/(?P<page_num>\d{1,2})$', SurveyViews.questions, name='survey_questions'),
  url(r'^survey/begin$', SurveyViews.public_begin, name='public_survey_begin'),
  url(r'^survey/next$', SurveyViews.next, name='survey_next'),
  url(r'^survey/continue$', SurveyViews.public_continue, name='public_survey_continue'),
  url(r'^survey/clear$', SurveyViews.clear, name='clear'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )