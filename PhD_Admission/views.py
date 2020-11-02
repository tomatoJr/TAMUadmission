from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
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
    
    