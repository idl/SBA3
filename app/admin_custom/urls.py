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
  url(r'^delete-school/(?P<school_id>[0-9]{1,3})$', AdminViews.superadmin_delete_school, name='superadmin_delete_school'),

  url(r'^(?P<school_id>[0-9]{1,3})/(?P<survey_year>[0-9]{4})$', AdminViews.admin_school_overview, name='admin_school_overview'),
  url(r'^(?P<school_id>[0-9]{1,3})/results-aggregate/(?P<survey_year>[0-9]{4})$', AdminViews.admin_results_aggregate, name='admin_results_aggregate'),
  url(r'^(?P<school_id>[0-9]{1,3})/change-year$', AdminViews.admin_select_survey_year, name='admin_select_survey_year'),
  url(r'^(?P<school_id>[0-9]{1,3})/create-students-bulk$', AdminViews.admin_create_students_bulk, name='admin_create_students_bulk'),
  url(r'^(?P<school_id>[0-9]{1,3})/create-student-single$', AdminViews.admin_create_student_single, name='admin_create_student_single'),
  url(r'^(?P<school_id>[0-9]{1,3})/export-students$', AdminViews.admin_export_students, name='admin_export_students'),
  url(r'^(?P<school_id>[0-9]{1,3})/delete-student/(?P<student_id>[0-9]{1,4})$', AdminViews.admin_delete_student, name='admin_delete_student'),
  url(r'^(?P<school_id>[0-9]{1,3})/edit-student/(?P<student_id>[0-9]{1,4})$', AdminViews.admin_edit_student, name='admin_edit_student'),
  url(r'^edit-account$', AdminViews.admin_edit_account, name='admin_edit_account'),
]
