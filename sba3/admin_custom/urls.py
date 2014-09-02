from django.conf.urls import patterns, url, include

urlpatterns = patterns('admin_custom.views',
    url(r'^/login/?$', 'login_view', name='login_view'),
    url(r'^/logout/?$', 'logout_view', name='logout_view'),
    url(r'^/(?P<username>[A-za-z0-9]{1,30})?$', 'admin', name='admin'),
    url(r'^/createuser/$', 'create_user', name='create_user'),
)
