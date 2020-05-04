from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'admindashboard/index.html')


def users(request):
    return HttpResponse("<h2>Admin dashboard users<h2>")


def logs(request):
    return HttpResponse("<h2>Admin dashboard logs<h2>")
