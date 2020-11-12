from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect

# from .models import Test
from .models import Applicant


# Create your views here.
def homecard(request):
    import requests
    import json
    api_request = requests.get("https://api.github.com/users?since=0")
    #api = json.loads(api_request.content)
    api = [{'studentName': 'A', 'studentGre': '320', 'studentGPA': '3.5'}, \
        {'studentName': 'B', 'studentGre': '321', 'studentGPA': '3.1'},\
        {'studentName': 'C', 'studentGre': '322', 'studentGPA': '3.2'},\
        {'studentName': 'D', 'studentGre': '323', 'studentGPA': '3.3'},\
        {'studentName': 'E', 'studentGre': '324', 'studentGPA': '3.4'},\
        {'studentName': 'F', 'studentGre': '325', 'studentGPA': '3.5'},\
        {'studentName': 'G', 'studentGre': '326', 'studentGPA': '3.6'},\
        {'studentName': 'H', 'studentGre': '327', 'studentGPA': '3.7'},\
        {'studentName': 'I', 'studentGre': '328', 'studentGPA': '3.8'},\
        {'studentName': 'J', 'studentGre': '329', 'studentGPA': '3.9'},\
        {'studentName': 'K', 'studentGre': '330', 'studentGPA': '4.0'},\
        {'studentName': 'L', 'studentGre': '331', 'studentGPA': '4.0'},\
        {'studentName': 'M', 'studentGre': '332', 'studentGPA': '4.0'},\
        {'studentName': 'N', 'studentGre': '333', 'studentGPA': '4.0'},\
        {'studentName': 'O', 'studentGre': '333', 'studentGPA': '4.0'},
    ]

    return render(request, 'homecard.html', {"api" : api})
    # return render(request, 'home.html', {})
    
def hometable(request):
    import requests
    import json
    api_request = requests.get("https://api.github.com/users?since=0")
    #api = json.loads(api_request.content)
    api = [{'studentName': 'A', 'studentGre': '320', 'studentGPA': '3.5'}, \
        {'studentName': 'B', 'studentGre': '321', 'studentGPA': '3.1'},\
        {'studentName': 'C', 'studentGre': '322', 'studentGPA': '3.2'},\
        {'studentName': 'D', 'studentGre': '323', 'studentGPA': '3.3'},\
        {'studentName': 'E', 'studentGre': '324', 'studentGPA': '3.4'},\
        {'studentName': 'F', 'studentGre': '325', 'studentGPA': '3.5'},\
        {'studentName': 'G', 'studentGre': '326', 'studentGPA': '3.6'},\
        {'studentName': 'H', 'studentGre': '327', 'studentGPA': '3.7'},\
        {'studentName': 'I', 'studentGre': '328', 'studentGPA': '3.8'},\
        {'studentName': 'J', 'studentGre': '329', 'studentGPA': '3.9'},\
        {'studentName': 'K', 'studentGre': '330', 'studentGPA': '4.0'},\
        {'studentName': 'L', 'studentGre': '331', 'studentGPA': '4.0'},\
        {'studentName': 'M', 'studentGre': '332', 'studentGPA': '4.0'},\
        {'studentName': 'N', 'studentGre': '333', 'studentGPA': '4.0'},\
        {'studentName': 'O', 'studentGre': '333', 'studentGPA': '4.0'}
]
    return render(request, 'hometable.html', {"api" : api})
    # return render(request, 'home.html', {})
    
def review(request):
    import requests
    api = {'studentName': 'A', 'studentGre': '320', 'studentGPA': '3.5'}
    return render(request, 'review.html', {"api" : api})
    
    
    
def send_email(request):
    print(request)
    def sendEmail(emailFrom, emailTo, emailToAddress, studentInfo):
        emailFrom = 'Prof.Ahmed'
        emailTo = 'Prof.Walker'
        emailToAddress = 'ziruiwang@tamu.edu'
        studentInfo = {'name':'Tom', 'GRE':'320', 'Nationality':'China', 'ResearchInteres':'AI' }
        send_mail(
        emailFrom + ' wants to nominate ' + studentInfo['name'] + ' with you',
        'Dear ' + emailTo + ',' + '\n' + emailFrom + ' wants to nominate ' + studentInfo['name'] + ' with you' + '\n' + 'Best regards' + '\n' + emailFrom + ' ',
        'tamu.csce.phdadmission@gmail.com',
        ['ziruiwang@tamu.edu'],
        fail_silently=False,
        )
    sendEmail(1,1,1,1)
    return redirect('/')
    # return render(request, 'homecard.html')


def use(request):
    #sendEmail(1,1,1,1)
    if request.method == 'POST':
        import requests
        import json
        user = request.POST['user']
        user_request = requests.get("https://api.github.com/users/" + user)
        username = json.loads(user_request.content)
        
        return render(request, 'user.html', {'user' : user, 'username' : username})
    else:
        notFound = 'please...'
        return render(request, 'user.html', {'notFound' : notFound})
    




def addApplicantInfo(request):

    applicant = Applicant.objects.create(
        Application_ID="8384741904",
        Average_Review_Score=0,
        Applied_Degree="Ph.D. Computer Science",
        Nationality="US",
        Name="Kanye West",
        Email="kanye@gmail.com",
        Research_Interest="Data Sicence; Artificial Intelligence",
        BS_University_and_GPA="Oxford University 4,0",
        MS_University_and_GPA="Stanford University 3.0",
        GRE_Score=152,
        TOEFL_Score=91,
        Gender='Male',
        Ethnicity='African-American',
        Residency='US',
        Citizenship='US',

        Potential_Faculty='',
        Faculty_Contact='',
        Faculty_giving_GANT_GAT='',
        Faculty_giving_GAR='',
    )

    applicant = Applicant.objects.create(
        Application_ID="7419048384",
        Average_Review_Score=0,
        Applied_Degree="M.S. Computer Science",
        Nationality="US",
        Name="Donald J. Trump",
        Email="trump@gmail.com",
        Research_Interest="Artificial Intelligence;Natural Language Processing",
        BS_University_and_GPA="University of Cambridge 4.0",
        MS_University_and_GPA="",
        GRE_Score=129,
        TOEFL_Score=100,
        Gender='Male',
        Ethnicity='American',
        Residency='US',
        Citizenship='US',

        Potential_Faculty='',
        Faculty_Contact='',
        Faculty_giving_GANT_GAT='',
        Faculty_giving_GAR='',
    )

    applicant = Applicant.objects.create(
        Application_ID="1904837484",
        Average_Review_Score=0,
        Applied_Degree="Ph.D. Computer Science",
        Nationality="US",
        Name="Captain America",
        Email="cap@gmail.com",
        Research_Interest="Algorithms and Theory",
        BS_University_and_GPA="Massachusetts Institute of Technology 3.0",
        MS_University_and_GPA="Stanford University 4.0",
        GRE_Score=149,
        TOEFL_Score=110,
        Gender='Female',
        Ethnicity='American',
        Residency='US',
        Citizenship='US',
    )

    applicant = Applicant.objects.create(
        Application_ID="3037912279",
        Average_Review_Score=0,
        Applied_Degree="Ph.D. Computer Science",
        Nationality="US",
        Name="Jessica Jones",
        Email="jessyJ@gmail.com",
        Research_Interest="Digital Humanities;Embedded Systems",
        BS_University_and_GPA="Imperial College London 3.0",
        MS_University_and_GPA="Imperial College London 4.0",
        GRE_Score=148,
        TOEFL_Score=108,
        Gender='Female',
        Ethnicity='Asian',
        Residency='India',
        Citizenship='International',
    )

    return HttpResponse('Successfully added info!')