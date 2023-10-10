# bot settings you can change -- options listed to the right
job_posting_age = '14'  # all, 1, 3, 7, 14 (these are days)
job_posting_type = 'alternance'  # all, full-time, contract, part-time, internship, temporary, Alternance
job_posting_experience = 'all'  # all, entry, mid, senior
job_posting_distance = '50'  # default 5, 10, 15, 25, 50, 100 (these are miles)

# change these to your information
account_email = 'gmetenou7@gmail.com'  # your indeed email
account_password = 'Password@123.'  # your indeed password
job_titles = ['développeur web alternance','Développeur web en alternance', 'alternance développeur web', 'Alternance développeur(se) web']  # separate job titles must be in quotations separated by a comma
job_location = 'Île-de-France'  # job zip

# apply personal answers
apply_linkedin = 'https://www.linkedin.com/in/gildas-metenou-056225176/'
apply_personalwebsite = ' '
apply_stateresident = 'yes'  # yes, no -- are you a state resident
apply_sponsorship = 'no'  # yes, no -- will you need work sponsorship
apply_relocate = 'yes'  # yes, no -- resident of ga or willing to relocate
apply_workauthorized = 'yes'  # yes, no -- authorized to work in us
apply_citizen = 'yes'  # yes, no -- us citizen
apply_education = 'master'  # other, highschool, associate, bachelor, master, doctorate -- education level
apply_leadershipdevelopment = '2'  # years
apply_salary = ' '
apply_gender = 'male' # male, female, decline
apply_veteran = 'no' # yes, no, decline -- veteran status
apply_disability = 'no' # yes, no, decline -- disability status

# language experience years
apply_java = '1'
apply_aws = '0.5'
apply_python = '0'
apply_django = '0'
apply_php = '4'
apply_react = '0'
apply_node = '0'
apply_angular = '0.5'
apply_javascript = '1'
apply_orm = '2'
apply_sdet = '0'
apply_selenium = '0'
apply_testautomation = '0'
apply_webdevyears = '4'

# don't change these - you break it you buy it
base_url = 'https://indeed.com'
login_url = 'https://secure.indeed.com/account/login?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F&tmpl=desktop&service=my&from=gnav-util-homepage'
page_timeout = 30
long_timeout = 300
job_urls = []

date_posted = {
    'all': '',
    '1': '&fromage=1',
    '3': '&fromage=3',
    '7': '&fromage=7',
    '14': '&fromage=14'
}

job_type = {
    'all': '',
    'full-time': '&jt=fulltime',
    'contract': '&jt=contract',
    'part-time': '&jt=parttime',
    'internship': '&jt=internship',
    'temporary': '&jt=temporary'
}

experience_level = {
    'all': '',
    'entry': '&explvl=entry_level',
    'mid': '&explvl=mid_level',
    'senior': '&explvl=senior_level'
}

job_distance = {
    'default': '',
    '5': '&radius=5',
    '10': '&radius=10',
    '15': '&radius=15',
    '25': '&radius=25',
    '50': '&radius=50',
    '100': '&radius=100'
}

apply_veteranoptions = {
    'no' : 'i am not',
    'yes' : 'i identify as one',
    'decline' : "i don't wish"
}

apply_disabilityoptions = {
    'no' : 'no',
    'yes' : 'yes',
    'decline' : "i don't wish"
}