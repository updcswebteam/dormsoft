from django.http import HttpResponse
from django.shortcuts import render

debug_users = [
    {
        'email': 'test@debug.com',
        'password': 'test',
    },
    {
        'email': 'test2@debug.com',
        'password': 'test2',
    },
]


def index(request):
    return render(request, 'admindashboard/index.html')


def users(request):
    context = {
        'users': debug_users,
    }
    return render(request, 'admindashboard/users.html', context)


def logs(request):
    return HttpResponse("<h2>Admin dashboard logs<h2>")
