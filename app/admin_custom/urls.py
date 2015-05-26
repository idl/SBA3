from django.conf.urls import patterns, url, include
from . import views as AdminViews

urlpatterns = [
  url(r'^login$', AdminViews.public_login, name='public_admin_login'),
  url(r'^logout$', AdminViews.public_logout, name='public_admin_logout'),

  url(r'^overview$', AdminViews.superadmin_overview, name='superadmin_overview'),
  url(r'^create-school$', AdminViews.superadmin_create_school, name='superadmin_create_school'),
  url(r'^(?P<school_id>[0-9]{1,3})$', AdminViews.admin_school_overview, name='admin_school_overview'),
  url(r'^create-admin$', AdminViews.superadmin_create_admin, name='superadmin_create_admin'),
  url(r'^edit-admin/(?P<admin_id>[0-9]{1,3})$', AdminViews.superadmin_edit_admin, name='superadmin_edit_admin'),
  url(r'^delete-admin/(?P<admin_id>[0-9]{1,3})$', AdminViews.superadmin_delete_admin, name='superadmin_delete_admin'),
  url(r'^edit-school/(?P<school_id>[0-9]{1,3})$', AdminViews.superadmin_edit_school, name='superadmin_edit_school'),

  url(r'^(?P<school_id>[0-9]{1,3})/(?P<survey_year>[0-9]{4})$', AdminViews.admin_school_overview, name='admin_school_overview'),
  url(r'^(?P<school_id>[0-9]{1,3})/change-year$', AdminViews.admin_select_survey_year, name='admin_select_survey_year'),
  url(r'^(?P<school_id>[0-9]{1,3})/add-students-bulk$', AdminViews.admin_add_students_bulk, name='admin_add_students_bulk'),
  url(r'^(?P<school_id>[0-9]{1,3})/add-student-single$', AdminViews.admin_add_student_single, name='admin_add_student_single'),
  url(r'^(?P<school_id>[0-9]{1,3})/delete-student/(?P<student_id>[0-9]{1,4})$', AdminViews.admin_delete_student, name='admin_delete_student'),
  url(r'^(?P<school_id>[0-9]{1,3})/edit-student/(?P<student_id>[0-9]{1,4})$', AdminViews.admin_edit_student, name='admin_edit_student'),
  # url(r'^/logout$', 'logout_view', name='logout_view'),
  # url(r'^/users$', 'users', name='users'),
  # url(r'^/registeradmin$', 'register_admin', name='register_admin'),
  # url(r'^/updateadmin/(?P<admin_id>[0-9]{1,3})$', 'update_admin', name='update_admin'),
  # url(r'^/deleteadmin/(?P<admin_id>[0-9]{1,3})$', 'delete_admin', name='delete_admin'),
  # url(r'^/schools$', 'schools', name='schools'),
  # url(r'^/createschool$', 'create_school', name='create_school'),
  # url(r'^/updateschool/(?P<school_id>[0-9]+)$', 'update_school', name='update_school'),
  # url(r'^/deleteschool/(?P<school_id>[0-9]+)$', 'delete_school', name='delete_school'),
  # url(r'^/(?P<school_id>[0-9]+)/roster$', 'manage_roster', name='manage_roster'),
  # url(r'^/(?P<school_id>[0-9]+)/rosterupdate$', 'update_roster', name='update_roster'),
  # url(r'^/(?P<school_id>[0-9]+)/rosterremove/(?P<uid>[0-9a-zA-Z ]+)$', 'remove_roster', name='remove_roster'),
  # url(r'^/(?P<school_id>[0-9]+)/rosterupload$', 'upload_roster', name='upload_roster'),
  # # url(r'^/data/(?P<school_id>[0-9]{1,2})$', 'survey_data_school', name='school_surveys'),
  # url(r'^/data/(?P<school_id>[0-9]{1,2})/viewall', 'survey_data_school_aggregate', name='school_data_aggregate'),
  # url(r'^/data/(?P<school_id>[0-9]{1,2})/(?P<student_id>[0-9]{1,2})$', 'survey_data_school_individual', name='school_student_data'),
]
