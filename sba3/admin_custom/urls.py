from django.conf.urls import patterns, url, include

urlpatterns = patterns('admin_custom.views',
    url(r'^/?$', 'admin_index', name='admin_index'),
    url(r'^/login$', 'login_view', name='login_view'),
    url(r'^/logout$', 'logout_view', name='logout_view'),
)
