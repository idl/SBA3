import re

def if_grad(session):
  p1q1 = str(session.get('ans_p1q1'))
  if p1q1 == 'master' or p1q1 == 'doctorate':
    # print "p1q1: IS MASTER OR DOCTORATE"
    return True
  # print "p1q1: NOT MASTER OR DOCTORATE"
  return False

def if_on_campus_class(session):
  p1q5 = str(session.get('ans_p1q5'))
  if p1q5 != 'yes':
    # print "p1q5: NOT ON CAMPUS CLASS"
    return False
  # print "p1q5: IS ON CAMPUS CLASS"
  return True


def add_condition_questions_to_session(result_set, page_num, session):
  if page_num is 1:
    session['ans_p'+str(page_num)+'q1'] = result_set['q1']
    session['ans_p'+str(page_num)+'q5'] = result_set['q5']
  # elif page_num is 2:
  #   # session['ans_p'+str(page_num)+'q3'] = result_set['q3']
  #   # session['ans_p'+str(page_num)+'q6'] = result_set['q6']
  #   # session['ans_p'+str(page_num)+'q11'] = result_set['q11']
  # elif page_num is 3:
  #   # session['ans_p'+str(page_num)+'q2'] = result_set['q2']
  #   # session['ans_p'+str(page_num)+'q3'] = result_set['q3']
  #   # session['ans_p'+str(page_num)+'q4'] = result_set['q4']
  #   # session['ans_p'+str(page_num)+'q5'] = result_set['q5']
  #   # session['ans_p'+str(page_num)+'q6'] = result_set['q6']
  # elif page_num is 4:
  #   # session['ans_p'+str(page_num)+'q2'] = result_set['q2']
  #   # session['ans_p'+str(page_num)+'q3'] = result_set['q3']
  #   # session['ans_p'+str(page_num)+'q4'] = result_set['q4']
  #   # session['ans_p'+str(page_num)+'q9'] = result_set['q9']
  #   # session['ans_p'+str(page_num)+'q10'] = result_set['q10']
  #   # session['ans_p'+str(page_num)+'q11'] = result_set['q11']
  # elif page_num is 5:
  #   # session['ans_p'+str(page_num)+'q2'] = result_set['q2']
  #   # session['ans_p'+str(page_num)+'q7'] = result_set['q7']
  #   # session['ans_p'+str(page_num)+'q8'] = result_set['q8']
  #   # session['ans_p'+str(page_num)+'q9'] = result_set['q9']
  #   # session['ans_p'+str(page_num)+'q13'] = result_set['q13']
  # elif page_num is 6:
  #   # session['ans_p'+str(page_num)+'q1'] = result_set['q1']
  #   # session['ans_p'+str(page_num)+'q2'] = result_set['q2']
  #   # session['ans_p'+str(page_num)+'q4'] = result_set['q4']
  #   # session['ans_p'+str(page_num)+'q6'] = result_set['q6']
  #   # session['ans_p'+str(page_num)+'q7'] = result_set['q7']
  # elif page_num is 7:
  #   # session['ans_p'+str(page_num)+'q2'] = result_set['q2']
  #   # session['ans_p'+str(page_num)+'q9'] = result_set['q9']
  # elif page_num is 8:
  #   # session['ans_p'+str(page_num)+'q2'] = result_set['q2']
  #   # session['ans_p'+str(page_num)+'q3'] = result_set['q3']
  #   # session['ans_p'+str(page_num)+'q4'] = result_set['q4']
  # elif page_num is 9:
  #   # session['ans_p'+str(page_num)+'q2'] = result_set['q2']
  #   # session['ans_p'+str(page_num)+'q3'] = result_set['q3']
  #   # session['ans_p'+str(page_num)+'q4'] = result_set['q4']
  #   # session['ans_p'+str(page_num)+'q5'] = result_set['q5']
  #   # session['ans_p'+str(page_num)+'q8'] = result_set['q8']
  # # elif page_num is 10:
  # #    no condition questions
  # elif page_num is 11:
  #   # session['ans_p'+str(page_num)+'q4'] = result_set['q4']
  #   # session['ans_p'+str(page_num)+'q5'] = result_set['q5']
  #   # session['ans_p'+str(page_num)+'q6'] = result_set['q6']
  #   # session['ans_p'+str(page_num)+'q12'] = result_set['q12']
  return