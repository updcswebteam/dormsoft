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
    context = {
        'active_link': "dashboard",
    }
    return render(request, 'admindashboard/index.html', context)


def users(request):
    context = {
        'active_link': "users",
        'users': debug_users,
    }
    return render(request, 'admindashboard/users.html', context)


def residents(request):
    context = {
        'active_link': "residents",
    }
    return render(request, 'admindashboard/residents.html', context)


def logs(request):
    context = {
        'active_link': "logs",
    }
    return render(request, 'admindashboard/logs.html', context)
