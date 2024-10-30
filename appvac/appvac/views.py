from django.shortcuts import render
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
    if request.method == "POST":
        username = request.POST.get("username", default=None)
        password = request.POST.get("password", default=None)

    return render(request, 'login_page.html', {})

