from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('sba3.views',
    # Examples:
    # url(r'^$', 'sba3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^questions$', 'questions', name='questions'),
    url(r'^page/(?P<pagenum>[0-9]{1,2})$', 'page', name='page')
)
