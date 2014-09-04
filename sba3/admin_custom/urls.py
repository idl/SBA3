from django.conf.urls import patterns, url, include

urlpatterns = patterns('admin_custom.views',
    url(r'^/?$', 'admin', name='admin'),
    url(r'^/login$', 'login_view', name='login_view'),
    url(r'^/logout$', 'logout_view', name='logout_view'),
    url(r'^/createschool$', 'create_school', name='create_school'),
)
