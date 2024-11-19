from django.shortcuts import render

def users_list(request):
    return render(request, 'users_list.html', {})