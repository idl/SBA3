from django.conf.urls import patterns, url, include
from django.contrib import admin
from sba3.admin_custom import urls
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^questions$', 'sba3.views.questions', name='questions'),
    url(r'^page/(?P<pagenum>[0-9]{1,2})$', 'sba3.views.page', name='page'),
    url(r'^previous$', 'sba3.views.previous' , name='previous'),
    url(r'^next$', 'sba3.views.next' , name='next'),
    url(r'^submit$', 'sba3.views.submit' , name='submit'),
    url(r'^clear$', 'sba3.views.clearSession', name='clear'),
    url(r'^report$', 'sba3.views.report', name='report'),

    url(r'^admin/?', include(admin.site.urls)),

    url(r'^admincustom/?', include(admin.site.urls)),
)
