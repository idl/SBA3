from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^/?$', 'admin_custom.views.admin_index', name='admin_index'),
    url(r'^/login$', 'admin_custom.views.login', name='login'),
    url(r'^/logout$', 'admin_custom.views.logout', name='logout'),
)
