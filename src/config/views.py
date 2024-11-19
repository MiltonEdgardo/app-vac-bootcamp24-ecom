from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as login_django

def home_page(request):
    name_list = [
        {"name": "Lucas", "last_name": "Duck"},
        {"name": "Mickey", "last_name": "Mouse"},
        {"name": "Bugs", "last_name": "Bunny"}
    ]
    context = {
        "all_users": name_list,
        "user_authenticated": "Edhar"
    }
    return render(request, 'home_page.html', context)

def users_list(request):
    return render(request, 'users_list.html', {})

def patients_list(request):
    return render(request, 'patients_list.html', {})

def login_page(request):
    print("method",request.method)
    print("--------------")
    print(request)
    #print(request.__class__.__name__)
    #print(request.__dict__)
    """print("PARAMETROS GET -->", request.GET)
    username = request.GET.get("username", default = None)
    """

    is_authenticated = False
    something_go_wrong = True
    username = ""

    if request.method == "POST":
        username = request.POST.get("username", default=None)
        password = request.POST.get("password", default=None)
        user = authenticate(request, username = username, password = password)
        is_authenticated = True

        if user:
            something_go_wrong = False
            login_django(request, user)
            return redirect('home')
        else:
            print("Authentication go wrong")


    context = {
        "is_authenticated": is_authenticated,
        "something_go_wrong": something_go_wrong,
        "username": username
    }
    return render(request, 'login_page.html', context)

