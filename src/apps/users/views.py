from django.shortcuts import render

from .models import User

def users_list(request):
    users = User.objects.all() #filter(id_in = [1, 2, 3])

    """
    u = User.objects.filter(id = 1).first()
    
    print("ALL USERS:")
    if u is None:
        print("User Does not exist")
    else:
        print(u)
        u = u[0]
    print(users)
    print(users.query)
    print("Long:", len(users))
    print("Count:", users.count())

    for user in users:
        print(user.last_login)
        
    """

    context = {
        "users": users
    }
    return render(request, 'users/list.html', context)