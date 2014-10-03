from django.conf.urls import patterns, url, include

urlpatterns = patterns('admin_custom.views',
    url(r'^/?$', 'admin', name='admin'),
    url(r'^/login$', 'login_view', name='login_view'),
    url(r'^/logout$', 'logout_view', name='logout_view'),
    url(r'^/registeradmin/$', 'register_admin', name='register_admin'),
    url(r'^/updateadmin/(?P<admin_id>[0-9]{1,3})$', 'update_admin', name='update_admin'),
    url(r'^/deleteadmin/(?P<admin_id>[0-9]{1,3})$', 'delete_admin', name='delete_admin'),
    url(r'^/createschool$', 'create_school', name='create_school'),
    url(r'^/data/(?P<school_id>[0-9]{1,2})$', 'admin', name='school_data'),
    url(r'^/data/(?P<school_id>[0-9]{1,2})/viewall', 'admin', name='school_data_viewall'),
    url(r'^/data/(?P<school_id>[0-9]{1,2})/(?P<student_id>[0-9]{1,2})$', 'admin', name='school_student_data'),

)
