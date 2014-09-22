from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from admin_custom import urls as admin_custom_urls

admin.autodiscover()

urlpatterns = patterns('sba3.views',
    url(r'^$', 'home', name='home'),

    url(r'^questions$', 'questions', name='questions'),
    url(r'^page/(?P<pagenum>[0-9]{1,2})$', 'page', name='page'),
    url(r'^previous$', 'previous' , name='previous'),
    url(r'^next$', 'next' , name='next'),
    url(r'^submit$', 'submit' , name='submit'),
    url(r'^clear$', 'clearSession', name='clear'),
    url(r'^report$', 'report', name='report'),

    url(r'^save_survey$', 'save_survey', name='save_survey'),
    url(r'^start_survey$', 'start_survey', name='start_survey'),
    url(r'^continue_survey$', 'continue_survey', name='continue_survey'),

    url(r'^admin2', include(admin.site.urls)),

    url(r'^admin', include(admin_custom_urls)),
    url(r'^login', 'login_view'),
    url(r'^logout', 'logout_view'),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
