from django import forms

CLASSIFICATION = (
    ('', '----'),
    ('freshman', 'Freshman'),
    ('sophmore', 'Sophmore'),
    ('junior', 'Junior'),
    ('senior', 'Senior'),
    ('master', 'Master'),
    ('doctorate', 'Doctorate'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment')
                )
MAJOR = (
    ('', '----'),
    ('accounting','Accounting Major'),
    ('aerospaceengineering','Aerospace Engineering Major'),
    ('agribusiness','Agribusiness Major'),
    ('art','Art Major'),
    ('agriengineering','Agricultural Engineering Technology and Business Major'),
    ('agriinformation','Agricultural Information Science Major'),
    ('agriculture','Agricultural Science Major'),
    ('agronomy','Agronomy Major'),
    ('dairyscience','Animal and Dairy Science Major'),
    ('anthropology','Anthropology Major'),
    ('architecture','Architecture Major'),
    ('art','Art Major'),
    ('biochemistry','Biochemistry Major'),
    ('bioengineering','Biological Engineering Major'),
    ('biology','Biological Sciences Major'),
    ('building','Building Construction Science Major'),
    ('businessadmin','Business Administration Major'),
    ('businessecon','Business Economics Major'),
    ('businessinfo','Business Information Systems Major'),
    ('chemengineering','Chemical Engineering Major'),
    ('chemistry','Chemistry Major'),
    ('civilengineering','Civil Engineering Major'),
    ('communication','Communication Major'),
    ('computerengineering','Computer Engineering Major'),
    ('computerscience','Computer Science Major'),
    ('criminology','Criminology Major'),
    ('culinology','Culinology Major'),
    ('economics','Economics Major (Arts and Sciences)'),
    ('educationalpsyc','Educational Psychology Major'),
    ('electricalengineering','Electrical Engineering Major'),
    ('elementaryed','Elementary Education Major'),
    ('english','English Major'),
    ('enviromentalecon','Environmental Economics and Management Major'),
    ('finance','Finance Major'),
    ('foodscience','Food Science, Nutrition and Health Promotion Major'),
    ('foreignlanguage','Foreign Language Major'),
    ('forestry','Forestry Major'),
    ('generallibarts','General Liberal Arts Major'),
    ('generalscience','General Science Major'),
    ('geoscience','Geosciences Major'),
    ('history','History Major'),
    ('horticulture','Horticulture Major'),
    ('humanscience','Human Sciences Major'),
    ('industrialengineering','Industrial Engineering Major'),
    ('industrialtech','Industrial Technology Major'),
    ('informationtech','Information Technology Services Major'),
    ('interdisciplinary','Interdisciplinary Studies'),
    ('interiordesign','Interior Design Major'),
    ('kinesiology','Kinesiology Major'),
    ('landscapearchitecture','Landscape Architecture Major'),
    ('landscapecontracting','Landscape Contracting Major'),
    ('management','Management Major'),
    ('marketing','Marketing Major'),
    ('mathematics','Mathematics Major'),
    ('mechanicalengineering','Mechanical Engineering Major'),
    ('medicaltech','Medical Technology Major'),
    ('microbiology','Microbiology Major'),
    ('musiceducation','Music Education Major'),
    ('music','Music Major'),
    ('philosophy','Philosophy Major'),
    ('physics','Physics Major'),
    ('polyscience','Political Science Major'),
    ('pultryscience','Poultry Science Major'),
    ('psychology','Psychology Major'),
    ('secondaryeducation','Secondary Education Major'),
    ('socialwork','Social Work Major'),
    ('sociology','Sociology Major'),
    ('softwareengineering','Software Engineering Major'),
    ('specialeducation','Special Education Major'),
    ('techteachereducation','Technology Teacher Education Major'),
    ('veterinarymedical','Veterinary Medical Technology'),
    ('wildlife','Wildlife, Fisheries and Aquaculture Major'),
    ('other','Something Else'),
    ('undecided','Undecided'),
    ('nocomment','No Comment')
              )

YES_NO = (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment')
        )

YES_NO_UNAVAILABE = (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('notavailable', 'None where avaliable'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment')
        )

AGREE_DISAGREE = (
    ('strongdisagree', 'Strongly Disagree'),
    ('disagree', 'Disagree'),
    ('neutral', 'Neither Agree nor Disagree'),
    ('agree', 'Agree'),
    ('strongagree', 'Strongly Agree'),
    ('notsure', 'Not Sure'),
    ('nocomment', 'No Comment')
        )

ROLE_MODEL = (
      ('', '----'),
      ('parent', 'Parent(s)'),
      ('grandparent', 'Grandparents'),
      ('sibling', 'Siblings'),
      ('auntuncle', 'Aunts or Uncles'),
      ('familyfriend', 'Family friends'),
      ('peer', 'Peers'),
      ('teammate', 'Teammates'),
      ('teacher', 'Teacher'),
      ('coach', 'Coach'),
      ('signother', 'Significant Other'),
      ('family', 'Family'),
      ('none', 'None of these'),
      ('notsure', 'Not sure'),
      ('nocomment', 'No comment'),
        )

class page_one(forms.Form):
    QUESTIONS = [
        'What is your class status?',
        'What is your major?',
        'Did you transfer from a community/junior college?',
        'Are you enrolled in a "Distance or Online" degree program at MSU?',
        'Have you ever taken a course that meets on campus?',
        'Did you attend a pre-kindergarten program?',
        'Did you complete any advanced placement courses in high school?',
        'Do you consider yourself a first generation college student?',
        'Prior to High School, did you personally know anyone who worked in the fields of Science, Technology, Engineering, or Math?',
        'Please consider the following statement: Education was encouraged in my family. Would you...',
        'In terms of your academic achievement, who contributed to your success the most?'
                ]

    p1q1 = forms.ChoiceField(
        required=True, 
        label=QUESTIONS[0], 
        widget=forms.Select(attrs={'class': 'form-control', 'name':'p1[]', 'id': 'p1q1'}), 
        choices=CLASSIFICATION
        )
    p1q2 = forms.ChoiceField(
        required=True, 
        label=QUESTIONS[1], 
        widget=forms.Select(attrs={'class': 'form-control', 'name':'p1[]', 'id': 'p1q2'}), 
        choices=MAJOR
        )
    p1q3 = forms.ChoiceField(
        required=True, 
        label=QUESTIONS[2], 
        widget=forms.Select(attrs={'class': 'form-control', 'name':'p1[]', 'id': 'p1q3'}), 
        choices=YES_NO
        )
    p1q4 = forms.ChoiceField(
        required=True, 
        label=QUESTIONS[3], 
        widget=forms.Select(attrs={'class': 'form-control', 'name':'p1[]', 'id': 'p1q4'}), 
        choices=YES_NO
        )
    p1q5 = forms.ChoiceField(
        required=True, 
        label=QUESTIONS[4], 
        widget=forms.Select(attrs={'class': 'form-control', 'name':'p1[]', 'id': 'p1q5'}), 
        choices=YES_NO
        )
    p1q6 = forms.ChoiceField(
        required=True, 
        label=QUESTIONS[5], 
        widget=forms.Select(attrs={'class': 'form-control', 'name':'p1[]', 'id': 'p1q6'}), 
        choices=YES_NO
        )
    p1q7 = forms.ChoiceField(
        required=True, 
        label=QUESTIONS[6], 
        widget=forms.Select(attrs={'class': 'form-control', 'name':'p1[]', 'id': 'p1q7'}), 
        choices=YES_NO_UNAVAILABE
        )
    p1q8 = forms.ChoiceField(
        required=True, 
        label=QUESTIONS[7], 
        widget=forms.Select(attrs={'class': 'form-control', 'name':'p1[]', 'id': 'p1q8'}), 
        choices=YES_NO
        )
    p1q9 = forms.ChoiceField(
        required=True, 
        label=QUESTIONS[8], 
        widget=forms.Select(attrs={'class': 'form-control', 'name':'p1[]', 'id': 'p1q9'}), 
        choices=YES_NO
        )
    p1q10 = forms.ChoiceField(
        required=True, 
        label=QUESTIONS[9], 
        widget=forms.Select(attrs={'class': 'form-control', 'name':'p1[]', 'id': 'p1q10'}), 
        choices=AGREE_DISAGREE
        )
    p1q11 = forms.ChoiceField(
        required=True, 
        label=QUESTIONS[10], 
        widget=forms.Select(attrs={'class': 'form-control', 'name':'p1[]', 'id': 'p1q11'}), 
        choices=ROLE_MODEL
        )