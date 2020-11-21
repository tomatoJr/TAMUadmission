from django.shortcuts import render, get_object_or_404
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
    api = [{'studentName': 'A', 'studentGre': '320', 'studentGPA': '3.5'}, ]
    applicants = Applicant.objects.all()
    context = {"api": api, "applicants": applicants}

    return render(request, 'homecard.html', context)


def hometable(request):
    # import requests
    # import json
    # api_request = requests.get("https://api.github.com/users?since=0")

    applicants = Applicant.objects.all()
    context = {"applicants": applicants}
    return render(request, 'hometable.html', context)


def review(request, app_seq_no=None):
    import requests
    api = {'studentName': 'A', 'studentGre': '320', 'studentGPA': '3.5'}
    applicant = get_object_or_404(Applicant, pk=app_seq_no)

    return render(request, 'review.html', {"api": api, "applicant": applicant})


def send_email(request):
    print(request)

    def sendEmail(emailFrom, emailTo, emailToAddress, studentInfo):
        emailFrom = 'Prof.Ahmed'
        emailTo = 'Prof.Walker'
        emailToAddress = 'ziruiwang@tamu.edu'
        studentInfo = {'name': 'Tom', 'GRE': '320',
                       'Nationality': 'China', 'ResearchInteres': 'AI'}
        send_mail(
            emailFrom + ' wants to nominate ' +
            studentInfo['name'] + ' with you',
            'Dear ' + emailTo + ',' + '\n' + emailFrom + ' wants to nominate ' +
            studentInfo['name'] + ' with you' + '\n' +
            'Best regards' + '\n' + emailFrom + ' ',
            'tamu.csce.phdadmission@gmail.com',
            ['ziruiwang@tamu.edu'],
            fail_silently=False,
        )
    sendEmail(1, 1, 1, 1)
    return redirect('/')
    # return render(request, 'homecard.html')


def use(request):
    # sendEmail(1,1,1,1)
    if request.method == 'POST':
        import requests
        import json
        user = request.POST['user']
        user_request = requests.get("https://api.github.com/users/" + user)
        username = json.loads(user_request.content)

        return render(request, 'user.html', {'user': user, 'username': username})
    else:
        notFound = 'please...'
        return render(request, 'user.html', {'notFound': notFound})


def addApplicantInfo(request):

    applicant = Applicant.objects.create(
        Application_ID="8384741904",
        Average_Review_Score=0,
        Applied_Degree="Ph.D. Computer Science",
        Nationality="US",
        Name="Kanye West",
        Email="kanye@gmail.com",
        Research_Interest="Data Sicence;Artificial Intelligence",
        BS_University_and_GPA="Oxford University 4,0",
        MS_University_and_GPA="Stanford University 3.0",
        GRE_Score=152,
        TOEFL_Score=91,
        Gender='Male',
        Ethnicity='African-American',
        Residency='US',
        Citizenship='US',
    )

    applicant = Applicant.objects.create(
        Application_ID="7419048384",
        Average_Review_Score=0,
        Applied_Degree="Ph.D. Computer Science",
        Nationality="US",
        Name="Donald J. Trump",
        Email="trump@gmail.com",
        Research_Interest="Artificial Intelligence;Natural Language Processing",
        BS_University_and_GPA="University of Cambridge 4.0",
        MS_University_and_GPA="University of Cambridge 3.8",
        GRE_Score=129,
        TOEFL_Score=100,
        Gender='Male',
        Ethnicity='American',
        Residency='US',
        Citizenship='US',

    )

    applicant = Applicant.objects.create(
        Application_ID="1904837484",
        Average_Review_Score=0,
        Applied_Degree="Ph.D. Computer Science",
        Nationality="US",
        Name="Captain America",
        Email="cap@gmail.com",
        Research_Interest="Algorithms and Theory;Artificial Intelligence",
        BS_University_and_GPA="Massachusetts Institute of Technology 3.0",
        MS_University_and_GPA="Stanford University 4.0",
        GRE_Score=149,
        TOEFL_Score=110,
        Gender='Female',
        Ethnicity='Asian',
        Residency='Korea',
        Citizenship='International',
    )

    applicant = Applicant.objects.create(
        Application_ID="3037912279",
        Average_Review_Score=0,
        Applied_Degree="Ph.D. Computer Science",
        Nationality="US",
        Name="Jessica Jones",
        Email="jessyJ@gmail.com",
        Research_Interest="Bioinformatics",
        BS_University_and_GPA="University of Cambridge 3.0",
        MS_University_and_GPA="Imperial College London 4.0",
        GRE_Score=148,
        TOEFL_Score=108,
        Gender='Female',
        Ethnicity='Asian',
        Residency='India',
        Citizenship='International',
    )

    applicant = Applicant.objects.create(
        Application_ID="2910579623",
        Average_Review_Score=0,
        Applied_Degree="Ph.D. Computer Science",
        Nationality="US",
        Name="Garrison Kane",
        Email="kane@gmail.com",
        Research_Interest="Data Sicence; Artificial Intelligence",
        BS_University_and_GPA="Oxford University 4,0",
        MS_University_and_GPA="Stanford University 3.0",
        GRE_Score=152,
        TOEFL_Score=91,
        Gender='Male',
        Ethnicity='African-American',
        Residency='US',
        Citizenship='US',
    )

    applicant = Applicant.objects.create(
        Application_ID="2579291344",
        Average_Review_Score=0,
        Applied_Degree="Ph.D. Computer Science",
        Nationality="US",
        Name="Fancy Dan",
        Email="fancy@gmail.com",
        Research_Interest="Artificial Intelligence;Natural Language Processing",
        BS_University_and_GPA="University of Cambridge 4.0",
        MS_University_and_GPA="Harvard University 3.0",
        GRE_Score=129,
        TOEFL_Score=100,
        Gender='Male',
        Ethnicity='Latino or Hispanic',
        Residency='Mexico',
        Citizenship='International',

    )

    applicant = Applicant.objects.create(
        Application_ID="4454812890",
        Average_Review_Score=0,
        Applied_Degree="Ph.D. Computer Science",
        Nationality="US",
        Name="Deacon Frost",
        Email="deacon@gmail.com",
        Research_Interest="Algorithms and Theory",
        BS_University_and_GPA="Harvard University 3.0",
        MS_University_and_GPA="University of Chicago 4.0",
        GRE_Score=149,
        TOEFL_Score=110,
        Gender='Female',
        Ethnicity='American',
        Residency='US',
        Citizenship='US',
    )

    applicant = Applicant.objects.create(
        Application_ID="3310526906",
        Average_Review_Score=0,
        Applied_Degree="Ph.D. Computer Science",
        Nationality="US",
        Name="Betty Ross",
        Email="betty@gmail.com",
        Research_Interest="Cyber-Physical Systems",
        BS_University_and_GPA="University of Chicago 3.0",
        MS_University_and_GPA="California Institute of Technology 4.0",
        GRE_Score=148,
        TOEFL_Score=108,
        Gender='Female',
        Ethnicity='Asian',
        Residency='India',
        Citizenship='International',
    )

    applicant = Applicant.objects.create(
        Application_ID="1045163838",
        Average_Review_Score=0,
        Applied_Degree="Ph.D. Computer Science",
        Nationality="US",
        Name="Black Panther",
        Email="cap@gmail.com",
        Research_Interest="Data Science",
        BS_University_and_GPA="California Institute of Technology 3.0",
        MS_University_and_GPA="Stanford University 4.0",
        GRE_Score=149,
        TOEFL_Score=110,
        Gender='Male',
        Ethnicity='Asian',
        Residency='China',
        Citizenship='International',
    )

    applicant = Applicant.objects.create(
        Application_ID="3530396559",
        Average_Review_Score=0,
        Applied_Degree="Ph.D. Computer Science",
        Nationality="US",
        Name="Luke Cage",
        Email="luke@gmail.com",
        Research_Interest="Cybersecurity",
        BS_University_and_GPA="Texas A&M University 3.0",
        MS_University_and_GPA="Texas A&M University 4.0",
        GRE_Score=138,
        TOEFL_Score=109,
        Gender='Female',
        Ethnicity='Asian',
        Residency='Korea',
        Citizenship='International',
    )

    return HttpResponse('Successfully added info!')
