from django.conf.urls import patterns, url, include

urlpatterns = patterns('admin_custom.views',
    url(r'^/?$', 'admin', name='admin'),
    url(r'^/login$', 'login_view', name='login_view'),
    url(r'^/logout$', 'logout_view', name='logout_view'),
    url(r'^/registeradmin/$', 'register_admin', name='register_admin'),
    url(r'^/deleteadmin$', 'delete_admin', name='delete_admin'),
    url(r'^/createschool$', 'create_school', name='create_school'),
)
