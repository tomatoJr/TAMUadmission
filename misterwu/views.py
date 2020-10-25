from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    api_request = requests.get("https://api.github.com/users?since=0")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {"api" : api})
    # return render(request, 'home.html', {})

def user(request):
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
    