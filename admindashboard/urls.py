from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="admin-dashboard.index"),
    path('users', views.users, name="admin-dashboard.index"),
    path('logs', views.logs, name="admin-dashboard.index"),
]
