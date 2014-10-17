from django.conf.urls import patterns, url, include

urlpatterns = patterns('admin_custom.views',
    url(r'^/?$', 'admin', name='admin'),
    url(r'^/login$', 'login_view', name='login_view'),
    url(r'^/logout$', 'logout_view', name='logout_view'),
    url(r'^/registeradmin/$', 'register_admin', name='register_admin'),
    url(r'^/updateadmin/(?P<admin_id>[0-9]{1,3})$', 'update_admin', name='update_admin'),
    url(r'^/deleteadmin/(?P<admin_id>[0-9]{1,3})$', 'delete_admin', name='delete_admin'),
    url(r'^/createschool$', 'create_school', name='create_school'),
    url(r'^/updateschool/(?P<school_id>[0-9]+)$', 'update_school', name='update_school'),
    url(r'^/deleteschool/(?P<school_id>[0-9]+)$', 'delete_school', name='delete_school'),
    url(r'^/(?P<school_id>[0-9]+)/roster$', 'manage_roster', name='manage_roster'),
    url(r'^/(?P<school_id>[0-9]+)/rosterupdate$', 'update_roster', name='update_roster'),
    url(r'^/(?P<school_id>[0-9]+)/rosterremove/(?P<uid>[0-9a-zA-Z]+)$', 'remove_roster', name='remove_roster'),
    url(r'^/(?P<school_id>[0-9]+)/rosterupload$', 'upload_roster', name='upload_roster'),
)
