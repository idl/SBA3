from django.template.defaultfilters import safe

subject = "SBA3-1 Survey - Continuation Key"
from_email = 'sba3survey@msussrc.com'
def message(uid, school_name, school_id, continue_pass):
  return safe("You have begun the SBA3-1 Survey. Please click the folling to continue the survey where you left off if you are not able to complete all of the questions at once:<br> <a href='localhost:8000/survey/continue?continue_pass=%s&school=%s&student_uid=%s'>http://localhost:8000/survey/continue?continue_pass=%s&school=%s&student_uid=%s</a>. Your information is as follows:<br> <ul> <li><b>Student Identifier</b>: %s</li><li><b>School Name</b>: %s</li><li><b>Continuation Passkey</b>: %s</li></ul>Click the following link to continue ") % continue_pass, school_id, uid, uid, school_name, continue_pass