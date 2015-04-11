from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from survey import views as SurveyViews
from .views import *

urlpatterns = [
  url(r'^$', public_index, name="public_index"),
  # url(r'/survey/home^$', public_survey_home, name="public_survey_home"),
  # url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
