var counter_fields = 0
var count_min_abs = 0
var count_max_abs = 0
var new_line = true
function addSearchField(div_id, field_type){
    var new_div = document.createElement('div');
    new_line = true;
    switch(field_type){
        case 'net_id':
            counter_fields++;
            new_div.innerHTML = '<input class="span2" type = "text" name="net_id[]" placeholder="Net Id" />';
            break;
        case 'min_absences':
            if(count_min_abs == 0){
                counter_fields++;
                count_min_abs++;
                new_div.innerHTML = '<input class="span2" type = "number" name="min_abs[]" placeholder="Minimum Absences" />';
            } else {
                new_line = false;
            }
            break;
        case 'max_absences':
            if(count_max_abs == 0){
                counter_fields++;
                count_max_abs++;
                new_div.innerHTML = '<input class="span2" type = "number" name="max_abs[]" placeholder="Maximum Absences" />';
            } else {
                new_line = false;
            }
            break;
        case 'course':
            counter_fields += 3;
            new_div.innerHTML = '<select class="span2" name="course_subject[]" SIZE="1">\
<option value="">Course Subject</option>\
<option value="ACC">ACC-Accounting</option>\
<option value="ASE">ASE-Aerospace Engineering</option>\
<option value="AS">AS-Aerospace Studies - AFROTC</option>\
<option value="AAS">AAS-African American Studies</option>\
<option value="ABE">ABE-Ag. and Bio. Engineering</option>\
<option value="AEC">AEC-Agricultural Economics</option>\
<option value="AIS">AIS-Agricultural Info Sci & Ed</option>\
<option value="AGN">AGN-Agronomy</option>\
<option value="ADS">ADS-Animal Science & Dairy Science</option>\
<option value="AN">AN-Anthropology</option>\
<option value="ALHP">ALHP-Appalachian Leadership Honors Prog</option>\
<option value="AR">AR-Archaeology</option>\
<option value="ARC">ARC-Architecture</option>\
<option value="ART">ART-Art</option>\
<option value="BCH">BCH-Biochemistry</option>\
<option value="BIO">BIO-Biological Sciences</option>\
<option value="BCS">BCS-Building Construction Science</option>\
<option value="BUS">BUS-Business Adminstration</option>\
<option value="BIS">BIS-Business Information Systems</option>\
<option value="BL">BL-Business Law</option>\
<option value="BQA">BQA-Business Quantitive Analysis</option>\
<option value="TKB">TKB-Business Technology</option>\
<option value="CHE">CHE-Chemical Engineering</option>\
<option value="CH">CH-Chemistry</option>\
<option value="FLC">FLC-Chinese</option>\
<option value="CE">CE-Civil Engineering</option>\
<option value="CO">CO-Communication</option>\
<option value="CCL">CCL-Community College Leadership</option>\
<option value="CME">CME-Computational Engineering</option>\
<option value="CPE">CPE-Computer Engineering</option>\
<option value="CSE">CSE-Computer Science & Engineering</option>\
<option value="CP">CP-Cooperative Education Program</option>\
<option value="COR">COR-Corrections</option>\
<option value="COE">COE-Counselor Education</option>\
<option value="CRM">CRM-Criminology</option>\
<option value="CA">CA-Culinary Arts</option>\
<option value="DSS">DSS-Disability Support Services</option>\
<option value="EC">EC-Economics</option>\
<option value="EDC">EDC-Education Core Curriculum</option>\
<option value="EDTB">EDTB-Education Student Block</option>\
<option value="EDST">EDST-Education Student Teaching</option>\
<option value="EDF">EDF-Educational Foundations</option>\
<option value="EDA">EDA-Educational Leadership (EDA)</option>\
<option value="EDL">EDL-Educational Leadership (EDL)</option>\
<option value="EPY">EPY-Educational Psychology</option>\
<option value="ECE">ECE-Electrical & Computer Engineer</option>\
<option value="EE">EE-Electrical Engineering</option>\
<option value="EDE">EDE-Elementary Education</option>\
<option value="EG">EG-Engineering Graphics</option>\
<option value="EM">EM-Engineering Mechanics</option>\
<option value="EN">EN-English</option>\
<option value="ESL">ESL-English as Second Language</option>\
<option value="EPP">EPP-Entomology & Plant Pathology</option>\
<option value="ENS">ENS-Environmental Science</option>\
<option value="EP">EP-Exercise Physiology</option>\
<option value="EXL">EXL-Experiental Learning</option>\
<option value="FIN">FIN-Finance</option>\
<option value="FNH">FNH-Food, Nutrition & Health Promo</option>\
<option value="FL">FL-Foreign Languages</option>\
<option value="FP">FP-Forest Products</option>\
<option value="FO">FO-Forestry</option>\
<option value="FLF">FLF-French</option>\
<option value="FYE">FYE-Freshman Year Experience</option>\
<option value="GLA">GLA-Gen Liberal Arts</option>\
<option value="GS">GS-Gender Studies</option>\
<option value="GA">GA-General Agriculture</option>\
<option value="GB">GB-General Business</option>\
<option value="GE">GE-General Engineering</option>\
<option value="GNS">GNS-Genetics</option>\
<option value="GR">GR-Geography</option>\
<option value="GG">GG-Geology</option>\
<option value="FLG">FLG-German</option>\
<option value="FLH">FLH-Greek</option>\
<option value="HCA">HCA-Healthcare Administration</option>\
<option value="HED">HED-Higher Education</option>\
<option value="HI">HI-History</option>\
<option value="HON">HON-Honors College</option>\
<option value="HS">HS-Human Sciences</option>\
<option value="IE">IE-Industrial Engineering</option>\
<option value="TKI">TKI-Industrial Technology</option>\
<option value="INS">INS-Insurance & Risk Management</option>\
<option value="IDS">IDS-Interdisciplinary Studies</option>\
<option value="ID">ID-Interior Design</option>\
<option value="IB">IB-International Business</option>\
<option value="ISE">ISE-International Student Exchange</option>\
<option value="FLI">FLI-Italian</option>\
<option value="FLJ">FLJ-Japanese</option>\
<option value="KI">KI-Kinesiology</option>\
<option value="LA">LA-Landscape Architecture</option>\
<option value="FLL">FLL-Latin</option>\
<option value="LSK">LSK-Learning Skills</option>\
<option value="MGT">MGT-Management</option>\
<option value="DTM">DTM-Manufacturing</option>\
<option value="MKT">MKT-Marketing</option>\
<option value="MA">MA-Mathematics</option>\
<option value="ME">ME-Mechanical Engineering</option>\
<option value="MIC">MIC-Microbiology</option>\
<option value="MEC">MEC-Middle Eastern Culture</option>\
<option value="MS">MS-Military Science - Army ROTC</option>\
<option value="MU">MU-Music</option>\
<option value="MUE">MUE-Music Education</option>\
<option value="MUA">MUA-Music, Applied</option>\
<option value="NSE">NSE-National Student Exchange</option>\
<option value="NREC">NREC-Natural Resource & Envir Cons</option>\
<option value="PHI">PHI-Philosophy</option>\
<option value="PE">PE-Physical Education</option>\
<option value="PH">PH-Physics</option>\
<option value="PHY">PHY-Physiology</option>\
<option value="PSS">PSS-Plant and Soil Sciences</option>\
<option value="PS">PS-Political Science</option>\
<option value="PO">PO-Poultry Science</option>\
<option value="PSY">PSY-Psychology</option>\
<option value="PPA">PPA-Public Policy & Administration</option>\
<option value="RDG">RDG-Readings in Education</option>\
<option value="REF">REF-Real Estate Finance</option>\
<option value="REL">REL-Religion</option>\
<option value="FLR">FLR-Russian</option>\
<option value="EDS">EDS-Secondary Education</option>\
<option value="SL">SL-Service Learning</option>\
<option value="SW">SW-Social Work</option>\
<option value="SO">SO-Sociology</option>\
<option value="FLS">FLS-Spanish</option>\
<option value="EDX">EDX-Special Education</option>\
<option value="SS">SS-Sport Studies</option>\
<option value="ST">ST-Statistics</option>\
<option value="SLCE">SLCE-Student Ldshp Comm Engagement</option>\
<option value="DTF">DTF-Technology Foundations</option>\
<option value="TKT">TKT-Technology Teacher Education</option>\
<option value="TR">TR-Transportation</option>\
<option value="UHP">UHP-University Honors Program</option>\
<option value="VTP">VTP-Veterans Transition Program</option>\
<option value="CVM">CVM-Veterinary Medicine</option>\
<option value="VS">VS-Veterinary Science</option>\
<option value="WFA">WFA-Wildlife,Fisheries & Aquacultu</option>\
<option value="WS">WS-Women\'s Studies</option>\
</select>\
<input class="span2" type = "text" name="course_id" placeholder="Course Id" />\
<input class="span2" type = "text" name="course_section" placeholder="Course Section" />';
            break;
        case 'instructor':
            counter_fields++;
            new_div.innerHTML = '<input class="span2" type = "text" name="course_instruct[]" placeholder="Instructor" />';
            break;
        default:
            break;
    }
    if(new_line == true){
        // if(counter_fields >= 6){
        //     counter_fields = 0;
        //     document.getElementById(div_id).appendChild(document.createElement('tr'));
        // }
        document.getElementById(div_id).appendChild(new_div);
    } else {
        return;
    }

}