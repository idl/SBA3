from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from admin import views as AdminViews
from admin import urls as AdminUrls
from survey import views as SurveyViews
from . import views as Sba3Views

urlpatterns = [
  url(r'^$', Sba3Views.public_index, name='public_index'),
  url(r'^survey/', include(SurveyViews)),
  url(r'^admin/', include(AdminUrls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
