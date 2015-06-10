# -*- coding: utf-8 -*-
from django.template.defaultfilters import safe

questions_1 = {
  'q1': 'What is your class status?',
  'q2': 'What is your major?',
  'q3': 'Did you transfer from a community/junior college?',
  'q4': 'Are you enrolled in a "Distance or Online" degree program at MSU?',
  'q5': 'Have you ever taken a course that meets on campus?',
  'q6': 'Did you attend a pre-kindergarten program?',
  'q7': 'Did you complete any advanced placement courses in high school?',
  'q8': 'Do you consider yourself a first generation college student?',
  'q9': 'Prior to High School, did you personally know anyone who worked in the fields of Science, Technology, Engineering, or Math?',
  'q10': 'Please consider the following statement: Education was encouraged in my family. Would you...',
  'q11': 'In terms of your academic achievement, who contributed to your success the most?',
}

questions_2 = {
  'q1': 'While growing up, did you have a mentor?',
  'q2': 'Do you have a mentor now?',
  'q3': 'Do you see role models on campus?',
  'q4': 'On a scale from 1 to 5, with 1 meaning "poor" and 5 meaning "excellent," how would you rate your time management skills?',
  'q5': 'Do you routinely use a calendar or daily planner (paper or digital)?',
  'q6': 'Do you review your class notes after class?',
  'q7': 'In general, do you study for tests by yourself?',
  'q8': 'Select the type of learning style that describes you best:',
  'q9': safe('On average, how many hours per DAY do you spend studying?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q10': safe('On average how many days in advance do you begin studying for upcoming exams?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q11': safe('In general, how many class sessions do you miss over the course of a semester?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
}

questions_3 = {
  'q1': 'Are you currently attending tutoring sessions?',
  'q2': 'On average, how many hours do you spend in tutoring sessions per week?',
  'q3': 'Would you attend tutoring sessions if they were freely available?',
  'q4': 'Have you looked for tutoring help?',
  'q5': 'Compared to high school, has the time you spend studying for classes...',
  'q6': safe('<span style="font-size:24px;font-weight: 300;">How often do you do the following?</span><br><br>(1) Show up late for class'),
  'q7': '(2) Turn assignments in late or incomplete',
  'q8': '(3) Miss an exam or quiz',
  'q9': '(4) Seek extra credit to improve a grade',
}

questions_4 = {
  'q1': 'Do you visit your professors on a regular basis?',
  'q2': 'Do you regularly ask questions in class?',
  'q3': 'Do your professors ask you questions during class?',
  'q4': 'Do you take complete class notes?',
  'q5': 'Do you have a study group?',
  'q6': 'Do you own a personal computer?',
  'q7': 'Do you have consistent access to broadband Internet?',
  'q8': 'Do you use the Internet to complete assignments?',
  'q9': 'Do you usually have all of the required books and materials by the second class meeting?',
  'q10': 'When professors ask questions, are you typically among the first to raise your hand?',
  'q11': 'In a typical classroom, where do you usually sit when seating is not assigned?',
}

questions_5 = {
  'q1': '<span style="font-size:24px;font-weight: 300;">How important to your academic success are the following:</span><br><br>Membership in Student Organization',
  'q2': 'Programs that help students transition from High School to College',
  'q3': 'Peer Mentoring',
  'q4': 'One-on-one mentoring by faculty',
  'q5': 'One-on-one mentoring from staff',
  'q6': 'Encouraging words from my professors/ instructors',
  'q7': 'Parent(s)/ Guardian(s) desire for me to earn a college degree',
  'q8': 'Hearing my parent(s)/guardian(s) bragging about me for attending college',
  'q9': 'Parent(s)/Guardian(s) giving gifts or money for making good grades',
  'q10': 'Friends\' encouragement to do well in college',
  'q11': 'Encouragement from my church family or community to stay in school',
  'q12': 'Participation in voluntary study groups',
  'q13': 'Reviewing course notes shortly after class',
  'q14': 'Visiting professors during their office hours',
}

questions_6 = {
  'q1': 'Do you participate in programs that help students transition from high school to college?',
  'q2': 'Do you have a peer mentor?',
  'q3': 'Do you have a one-on-one faculty mentor?',
  'q4': 'Do you have a one-on-one staff mentor?',
  'q5': 'Do you receive encouraging words from your professors?',
  'q6': 'Do you hear your parents/guardians bragging about you for attending college?',
  'q7': 'Do your parents/guardians give you gifts or money for making good grades?',
  'q8': 'Do your friends encourage you to do well in college?',
  'q9': 'Do you receive encouragement from your church family or community to stay in school?',
  'q10': safe('<span style="font-size:24px;font-weight: 300;">For the next 3 questions, to what extend do you agree with each statement?</span><br><br>My professors expect me to do well in most classes. '),
  'q11': 'My professors make me feel good about my academic work in class.',
  'q12': 'Earning a college degree is the best path to financial security.',
}


questions_7 = {
  'q1': safe('<span style="font-size:24px;font-weight: 300;">Overall, what letter grade do the following people expect you to make?</span><br><br>What Letter Grade do YOU expect to make at MSU?'),
  'q2': 'What Letter Grade do your PARENT(S)/ GUARDIAN(S) expect you to make at MSU?',
  'q3': 'What Letter Grade do your TEACHERS/ PROFESSORS expect you to make at MSU?',
  'q4': 'What Letter Grade do your CLOSE FRIENDS expect you to make at MSU?',
  'q5': 'What Letter Grade do your BROTHER(S)/ SISTER(S) expect you to make at MSU?',
  'q6': safe('What was your highest ACT Score?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q7': safe('What was your overall grade point average (GPA) in High School?<br>(<code>-1.0</code> for Not Sure, <code>-2.0</code> for No Comment)'),
  'q8': safe('What was your overall grade point average (GPA) in College?<br>(<code>-1.0</code> for Not Sure, <code>-2.0</code> for No Comment)'),
  'q9': safe('How many on-line classes have you completed with a grade of less than "C" at MSU?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
}

questions_8 = {
  'q1': 'Did you attend a Student Orientation session before starting college?',
  'q2': 'Did your parents (or guardians) attend an orientation session with you?',
  'q3': 'Do you share your grades with your parent(s) or legal guardian(s)?',
  'q4': 'Do your parents (or guardians) require you to maintain a certain GPA in college?',
  'q5': 'Do you believe you were academically prepared for college?',
  'q6': '<span style="font-size:24px;font-weight: 300;">Given your academic performance in college, to what extend do you agree with the following statements?</span><br><br>I should have read more books before college.',
  'q7': 'I should have taken more math courses in high school.',
  'q8': 'I should have taken more science courses in high school.',
  'q9': 'I should have paid more attention in classes.',
  'q10': 'I should have worked harder on written assignments.',
  'q11': 'I should have worked with a tutor.',
  'q12': 'I should have enrolled in a program to improve studying skills.',
}

questions_9 = {
  'q1': 'Do you belong to any student organizations?',
  'q2': safe('How many hours per week do you spend doing student organization related services or activities?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q3': 'Do you live on or off campus?',
  'q4': 'While attending college, do you live away from home?',
  'q5': safe('How many times per semester do you go home?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q6': safe('On average, how many hours per week do you spend partying?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q7': 'Do you drink alcoholic beverages?',
  'q8': safe('On days that you drink, about how many drinks do you consume?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q9': safe('On average, how many hours of sleep do you get on a weeknight?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q10': safe('How many days per week do you exercise for at least 15 minutes?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q11': safe('How many days during the week do you eat a nutritious (e.g., fruits, vegetable, nuts, lean meats etc) meal for breakfast?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q12': safe('How many days during the week do you eat a nutritious (e.g., fruits, vegetable, nuts, lean meats etc) meal for lunch?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q13': safe('How many days during the week do you eat a nutritious (e.g., fruits, vegetable, nuts, lean meats etc) meal for dinner?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
}

questions_10 = {
  'q1': safe('<span style="font-size:24px;font-weight: 300;">For the next three items, please indicate, on average, how much time you spend per day engaged in the following activities:</span><br><br>Social Media (Facebook, Twitter, Instagram…)<br><br>Hours:'),
  'q2': '',
  'q3': safe('Entertainment (TV, Games, Movies)<br><br>Hours:'),
  'q4': '',
  'q5': safe('Personal Communication (Phone calls, Text messages, Emails)<br><br>Hours:'),
  'q6': '',
  'q7': safe('<span style="font-size:24px;font-weight: 300;">In your opinion, what are the top three reasons students struggle in college?</span><br><br>Most Important Reason:'),
  'q8': 'Second Most Important Reason:',
  'q9': 'Third Most Important Reason:',
  'q10': safe('<span style="font-size:24px;font-weight: 300;">In your opinion, what are the top three reasons students succeed in college?</span><br><br>Most Important Reason:'),
  'q11': 'Second Most Important Reason:',
  'q12': 'Third Most Important Reason:',
}

questions_11 = {
  'q1': safe('What is your age?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q2': 'What is your gender?',
  'q3': 'Are you currently employed?',
  'q4': 'Do you work on or off campus?',
  'q5': safe('On average, how many hours per week do you work?<br>(<code>-1</code> for Not Sure, <code>-2</code> for No Comment)'),
  'q6': 'Do you work anytime between the hours of 5pm - 12am?',
  'q7': 'What is the highest level of education completed by your mother?',
  'q8': 'What is the highest level of education completed by your father?',
  'q9': 'In general, how would you describe the racial mix of your high school?',
  'q10': 'Which category best describes your race?',
  'q11': 'Do you have friends of other ethnic groups?',
  'q12': 'Do you receive the Pell grant?',
  'q13': 'While in high school, did you qualify for or receive free or reduced priced lunch?',
  'q14': 'In your opinion, did the majority of students in your high school receive free or reduced priced lunch?',
}