import re

def if_grad(session):
  p1q1 = session.get('ans_p1q1')
  if p1q1 == None:
    return False
  p1q1 = str(p1q1)
  if p1q1 == 'master' or p1q1 == 'doctorate':
    # print "p1q1: IS GRAD"
    return True
  return False

def if_not_distance(session):
  p1q4 = session.get('ans_p1q4')
  if p1q4 == None:
    return False
  p1q4 = str(p1q4)
  if p1q4 != 'yes':
    # print "p1q4: IS NOT DISTANCE"
    return True
  return False

def if_not_on_campus_class(session):
  p1q5 = session.get('ans_p1q5')
  if p1q5 == None:
    return False
  p1q5 = str(p1q5)
  if p1q5 != 'yes':
    # print "p1q5: IS NOT ON CAMPUS CLASS"
    return True
  return False

def if_not_tutoring(session):
  p3q1 = session.get('ans_p3q1')
  if p3q1 == None:
    return False
  p3q1 = str(p3q1)
  if p3q1 != 'yes':
    # print "p3q1: IS NOT TUTORING"
    return True
  return False

def if_tutoring(session):
  p3q1 = session.get('ans_p3q1')
  if p3q1 == None:
    return False
  p3q1 = str(p3q1)
  if p3q1 == 'yes':
    # print "p3q1: IS TUTORING"
    return True
  return False

def if_grad_and_not_orientation(session):
  p1q1 = session.get('ans_p1q1')
  p8q1 = session.get('ans_p8q1')
  if p1q1 == None or p8q1 == None:
    return False
  p1q1 = str(p1q1)
  p8q1 = str(p8q1)
  if (p1q1 == 'master' or p1q1 == 'doctorate') and (p8q1 != 'yes'):
    # print "p1q1, p8q1: IS NOT GRAD and IS NOT ORIENTATION"
    return True
  return False

def if_not_organization_member(session):
  p9q1 = session.get('ans_p9q1')
  if p9q1 == None:
    return False
  p9q1 = str(p9q1)
  if p9q1 != 'yes':
    # print "p9q1: IS NOT ORGANIZATION MEMBER"
    return True
  return False

def if_live_on_campus(session):
  p9q3 = session.get('ans_p9q3')
  if p9q3 == None:
    return False
  p9q3 = str(p9q3)
  if p9q3 == 'oncampus':
    # print "p9q3: IS LIVES ON CAMPUS"
    return True
  return False

def if_not_away_from_home_or_not_live_on_campus(session):
  p9q4 = session.get('ans_p9q4')
  p9q3 = session.get('ans_p9q3')
  if p9q4 == None or p9q3 == None:
    return False
  p9q4 = str(p9q4)
  p9q3 = str(p9q3)
  if (p9q4 != 'yes') or (p9q3 != 'oncampus'):
    # print "p9q3, p9q4: IS NOT AWAY FROM HOME or IS NOT LIVES ON CAMPUS"
    return True
  return False

def if_not_drink_alcohol(session):
  p9q7 = session.get('ans_p9q7')
  if p9q7 == None:
    return False
  p9q7 = str(p9q7)
  if p9q7 != 'yes':
    # print "p9q7: IS NOT DRINK ALCOHOL"
    return True
  return False

def if_not_employed(session):
  p11q3 = session.get('ans_p11q3')
  if p11q3 == None:
    return False
  p11q3 = str(p11q3)
  if p11q3 != 'yes':
    # print "p11q3: IS NOT EMPLOYED"
    return True
  return False





def add_condition_questions_to_session(result_set, page_num, session):
  if page_num is 1:
    session['ans_p'+str(page_num)+'q1'] = result_set['q1']
    session['ans_p'+str(page_num)+'q4'] = result_set['q4']
    session['ans_p'+str(page_num)+'q5'] = result_set['q5']
  elif page_num is 3:
    session['ans_p'+str(page_num)+'q1'] = result_set['q1']
  elif page_num is 8:
    session['ans_p'+str(page_num)+'q1'] = result_set['q1']
  elif page_num is 9:
    session['ans_p'+str(page_num)+'q1'] = result_set['q1']
    session['ans_p'+str(page_num)+'q3'] = result_set['q3']
    session['ans_p'+str(page_num)+'q4'] = result_set['q4']
    session['ans_p'+str(page_num)+'q7'] = result_set['q7']
  elif page_num is 11:
    session['ans_p'+str(page_num)+'q3'] = result_set['q3']
  return